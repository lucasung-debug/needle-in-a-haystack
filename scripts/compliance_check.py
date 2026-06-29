#!/usr/bin/env python3
"""compliance_check.py — validator-as-gate for needle-in-a-haystack research outputs.

Turns research.md's prose compliance block into a deterministic gate. Point it at a
finished research output (markdown) and it exits non-zero unless the output honours
the compliance contract: the block is present, every gate verdict is *resolved* (no
[PASS/FAIL] placeholders left), no gate is FAIL while FINAL is VALID, FINAL is VALID,
paid use without consent is rejected, and provenance is not obviously fabricated.

Stdlib only. Portable: invoke as `python ${CLAUDE_SKILL_DIR}/scripts/compliance_check.py <output.md>`.

Surface-parsable contract (for autoresearch wrappers):  prints  `compliance_pass: 0|1`.
Exit 0 = passes the gate; exit 1 = a violation was found (do not ship the output).
"""
import argparse
import json
import re
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

REQUIRED_GATES = ["FRAME", "ABDUCT", "FALSIFY", "INDEP", "C", "L1", "L2", "L3", "L4", "COST", "NULL", "FINAL"]
# Gates whose only acceptable resolved verdict is PASS:
PASS_ONLY = ["FRAME", "ABDUCT", "FALSIFY", "INDEP", "C", "L1", "L2", "L3", "L4"]

GATE_LINE = re.compile(r"^\[([A-Z0-9]+)\]\s*:\s*(.*)$")
BRACKET = re.compile(r"\[([^\]]*)\]")
URL = re.compile(r"https?://[^\s)>\]\"']+", re.I)
ISO_TS = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
FABRICATION_SMELLS = [
    "example.com", "<url>", "todo", "lorem ipsum", "placeholder-url", "http://example",
]


def analyze(text):
    violations = []

    # 1. Locate gate lines and their resolved verdicts (last bracket on the line).
    gates = {}
    for raw in text.splitlines():
        line = raw.strip()
        m = GATE_LINE.match(line)
        if not m:
            continue
        gate = m.group(1)
        remainder = m.group(2)
        br = BRACKET.findall(remainder)
        # verdict = last bracketed token if any (e.g. "... [PASS]"), else the bare
        # trailing text (e.g. "[FINAL]:  VALID", which carries no brackets).
        verdict = (br[-1] if br else remainder).strip().upper()
        gates[gate] = {"verdict": verdict, "tokens": [t.strip().upper() for t in br]}

    # 2. Block presence + required gates.
    if not gates:
        violations.append("no compliance block found (research.md requires one to close every output)")
        return violations, gates
    missing = [g for g in REQUIRED_GATES if g not in gates]
    if missing:
        violations.append("missing required gate(s): " + ", ".join(missing))

    # 3. Unresolved placeholders (a slash in the verdict = the template was never filled).
    for g, info in gates.items():
        if "/" in info["verdict"]:
            violations.append(f"[{g}] left unresolved (placeholder verdict '{info['verdict']}')")

    # 4. Verdict semantics.
    for g in PASS_ONLY:
        if g in gates and "/" not in gates[g]["verdict"]:
            if gates[g]["verdict"] != "PASS":
                violations.append(f"[{g}] is {gates[g]['verdict'] or 'empty'} — not PASS")
    if "NULL" in gates and "/" not in gates["NULL"]["verdict"]:
        if gates["NULL"]["verdict"] not in ("PASS", "NA"):
            violations.append(f"[NULL] is {gates['NULL']['verdict'] or 'empty'} — must be PASS or NA")
    if "COST" in gates:
        toks = gates["COST"]["tokens"]
        # paid used = YES but consent recorded = NO  -> spending without consent
        if "YES" in toks and "NO" in toks:
            violations.append("[COST] paid source used (YES) without recorded consent (NO) — consent interlock breached")
    if "FINAL" in gates and "/" not in gates["FINAL"]["verdict"]:
        fv = gates["FINAL"]["verdict"]
        if re.search(r"\bINVALID\b", fv):
            violations.append("[FINAL] is INVALID — output self-declares invalid and must be redone, not shipped")
        elif not re.search(r"\bVALID\b", fv):
            violations.append(f"[FINAL] is '{fv or 'empty'}' — must be VALID")

    fv = gates.get("FINAL", {}).get("verdict", "")
    final_valid = bool(re.search(r"\bVALID\b", fv)) and not re.search(r"\bINVALID\b", fv)
    c_pass = gates.get("C", {}).get("verdict") == "PASS"

    # 5. Fabrication smells (placeholder/fake citations).
    low = text.lower()
    for smell in FABRICATION_SMELLS:
        if smell in low:
            violations.append(f"fabrication smell: '{smell}' present in a shippable output")

    # 6. Provenance: a VALID output with retrieved claims needs real URLs + a timestamp.
    has_retrieved = "[retrieved" in low
    urls = URL.findall(text)
    if final_valid and has_retrieved and not urls:
        violations.append("output tags claims [retrieved] but carries no source URL (LAW 0)")
    if final_valid and c_pass and not urls:
        violations.append("[C]=PASS asserts every claim maps to a live source URL, but the output carries no URL at all (LAW 0)")
    if final_valid and re.search(r"(?im)^#{1,6}.*\bsources?\b|key sources", text) and not ISO_TS.search(text):
        violations.append("a Sources section is present but no ISO-8601 UTC retrieval timestamp (LAW 0)")

    # 7. Per-source live-link discipline (LAW 0 status vocabulary: live|dead|throttled|paywalled|unverified).
    for raw in text.splitlines():
        line = raw.strip()
        if not URL.search(line):
            continue
        low_line = line.lower()
        is_ruled_out = bool(re.search(r"ruled[ -]?out|contradict", low_line))
        # (a) a cited source is dead/4xx while [C]=PASS claims every claim maps to a LIVE source.
        if final_valid and c_pass and not is_ruled_out and re.search(r"\b(dead|404|4xx)\b", low_line):
            violations.append("a cited source is dead/4xx while [C]=PASS claims live sources (LAW 0)")
        # (b) a [retrieved] source line without an ISO-8601 UTC timestamp.
        if final_valid and "[retrieved" in low_line and not ISO_TS.search(line):
            violations.append("a [retrieved] source URL lacks an ISO-8601 UTC timestamp on its line (LAW 0 [C])")

    # 8. NEEDLE NOT FOUND vs [NULL] consistency: a headline/answer that declares no needle while [NULL]=NA
    #    (NA = a needle WAS found, so null is not applicable) is self-contradictory. Checks only the heading/
    #    Answer line, not prose or the NULL gate line itself, to stay structural (no false positives on mentions).
    null_verdict = gates.get("NULL", {}).get("verdict", "")
    headline_nnf = any(
        (s.startswith("#") or s.lower().startswith("**answer"))
        and re.search(r"needle not found|unanswerable", s, re.I)
        for s in (raw.strip() for raw in text.splitlines())
    )
    if final_valid and headline_nnf and null_verdict == "NA":
        violations.append("the answer declares NEEDLE NOT FOUND / UNANSWERABLE but [NULL]=NA (NA means a needle was found) — set [NULL]=PASS for a genuine null result")

    # 9. Skeptic-judge binding: a found-needle VALID output (FALSIFY=PASS, not a null result) must carry a *resolved
    #    PASS* [SKEPTIC] verdict — the falsify-skeptic.md scorecard — so the judge's verdict is auditable in the gated
    #    artifact instead of floating free. (Structural only: the token must be present and PASS; the judge owns the
    #    substance.) Null results ([NULL]=PASS) and non-VALID outputs are exempt.
    falsify_pass = gates.get("FALSIFY", {}).get("verdict") == "PASS"
    if final_valid and falsify_pass and null_verdict != "PASS":
        skeptic = gates.get("SKEPTIC")
        if skeptic is None:
            violations.append("a found-needle VALID output carries no [SKEPTIC] verdict — bind the skeptic-judge scorecard (falsify-skeptic.md) into the compliance block; it must not float free")
        elif "/" not in skeptic["verdict"] and skeptic["verdict"] != "PASS":
            violations.append(f"[SKEPTIC] is {skeptic['verdict'] or 'empty'} — the skeptic-judge did not pass; rework the finding, do not ship")

    # de-duplicate while preserving order
    violations = list(dict.fromkeys(violations))
    return violations, gates


def analyze_html(text):
    """Structural self-containment check for an HTML report (templates/report.html). The file must depend on
    NO external resource — only <a href> links to cited sources are allowed. Robust (structural, not semantic).
    Self-containment ONLY: LAW 0 provenance (live URL + ISO timestamp + [C]/[COST] interlocks) is enforced on the
    markdown path (analyze); render HTML FROM a report.md that already passed the gate — the extension is not a dodge."""
    v = []
    low = text.lower()
    if "{{" in text:
        v.append("HTML report has unfilled {{...}} placeholder(s) — fill or mark every slot before shipping")
    if re.search(r"<link\b[^>]*stylesheet", text, re.I):
        v.append("HTML uses an external <link> stylesheet — inline the CSS (report must be self-contained)")
    if re.search(r"<script\b[^>]*\bsrc\s*=", text, re.I):
        v.append("HTML loads an external <script src> — inline or drop it (report must be self-contained)")
    for m in re.finditer(r"<img\b[^>]*\bsrc\s*=\s*[\"']?([^\"'>\s]+)", text, re.I):
        if not m.group(1).lower().startswith("data:"):
            v.append("HTML <img> uses a non-inline src — embed as a data: URI or omit (report must be self-contained)")
            break
    if re.search(r"@import\b", text, re.I):
        v.append("HTML @import pulls external CSS — inline it (report must be self-contained)")
    if re.search(r"url\(\s*[\"']?\s*(?:https?:)?//", text, re.I):
        v.append("HTML CSS url(...) references an external resource — inline or drop it (report must be self-contained)")
    for smell in FABRICATION_SMELLS:
        if smell in low:
            v.append(f"fabrication smell: '{smell}' present in a shippable output")
    if "<!doctype html" not in low and "<html" not in low:
        v.append("not a well-formed HTML document (missing <!doctype html> / <html>)")
    return list(dict.fromkeys(v))


_LINK_UA = {"User-Agent": "needle-in-a-haystack-linkcheck/1.0"}


def _is_nxdomain(err):
    """True only for a genuine 'name does not exist' (EAI_NONAME). Transient resolver failure (EAI_AGAIN) and
    SERVFAIL (EAI_FAIL) are NOT fabrication evidence — they degrade to 'unverified', never failing the gate."""
    reason = getattr(err, "reason", None)
    return isinstance(reason, socket.gaierror) and getattr(reason, "errno", None) == socket.EAI_NONAME


def _probe_once(url, method, timeout):
    req = urllib.request.Request(url, method=method, headers=_LINK_UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return (getattr(r, "status", None) or r.getcode()), r.geturl()


def _classify_url(url, timeout):
    """Probe one URL. Returns one of:
      ('dead', code)        — 404/410: definitively not here.
      ('nxdomain', None)    — the domain does not resolve (strong fabrication/dead signal).
      ('suspect', why)      — 2xx but a deep path redirected to the bare origin (likely soft-404 / removed).
      ('unverified', why)   — transient/5xx/access(401/403/405/429/451/501)/TLS/proxy/timeout: a flaky or
                              policy-restricted network must NEVER fail the gate, so these never count as dead.
      ('live', code)        — reachable, real content path.
    Only 404/410 and NXDOMAIN ever become gate violations; everything the probe could not positively kill is
    'unverified'. HEAD is often refused/transient, so access/method/5xx codes are confirmed with a GET first."""
    try:
        code, final = _probe_once(url, "HEAD", timeout)
    except urllib.error.HTTPError as e:
        if e.code in (400, 401, 403, 405, 429, 451, 501) or e.code >= 500:
            try:
                code, final = _probe_once(url, "GET", timeout)
            except urllib.error.HTTPError as e2:
                code, final = e2.code, url
            except urllib.error.URLError as e2:
                return ("nxdomain", None) if _is_nxdomain(e2) else ("unverified", "unreachable")
            except Exception:
                return ("unverified", "unreachable")
        else:
            code, final = e.code, url
    except urllib.error.URLError as e:
        return ("nxdomain", None) if _is_nxdomain(e) else ("unverified", "unreachable")
    except Exception:
        return ("unverified", "unreachable")

    if code in (404, 410):
        return ("dead", code)
    if code in (401, 403, 405, 429, 451, 501) or 500 <= code < 600:
        return ("unverified", f"http {code}")
    if 200 <= code < 400:
        try:
            want = urllib.parse.urlsplit(url).path.strip("/")
            got = urllib.parse.urlsplit(final).path.strip("/")
        except Exception:
            want = got = ""
        if want and not got:  # deep path redirected to bare origin -> likely soft-404 / moved
            return ("suspect", "redirected to homepage")
        return ("live", code)
    return ("unverified", f"http {code}")


def check_links_live(text, timeout=5, limit=40, budget=60.0):
    """Opt-in (--check-links) best-effort liveness probe for cited URLs. Network-dependent, so it lives OUTSIDE the
    deterministic gate/eval. Returns a dict: dead [(url,code)] (404/410), nxdomain [url], suspect [(url,why)],
    unverified [(url,why)], skipped (count past limit/time budget), probed (count reached). Only dead + nxdomain
    become gate violations; a flaky or policy-restricted network can never fail the gate (it degrades to unverified).
    A global wall-clock budget bounds the worst case (HEAD+GET doubling × slow hosts)."""
    out = {"dead": [], "nxdomain": [], "suspect": [], "unverified": [], "skipped": 0, "probed": 0}
    seen = []
    for raw_url in URL.findall(text):
        u = raw_url.rstrip(".,;")
        if u not in seen:
            seen.append(u)
    start = time.monotonic()
    for u in seen:
        if out["probed"] >= limit or (time.monotonic() - start) > budget:
            out["skipped"] = len(seen) - out["probed"]
            break
        out["probed"] += 1
        kind, detail = _classify_url(u, timeout)
        if kind == "live":
            continue
        out[kind].append(u if kind == "nxdomain" else (u, detail))
    return out


def main():
    ap = argparse.ArgumentParser(description="Compliance gate for needle-in-a-haystack outputs.")
    ap.add_argument("path", help="path to a finished research output (markdown)")
    ap.add_argument("--json", action="store_true", help="emit JSON report")
    ap.add_argument("--check-links", action="store_true",
                    help="best-effort network liveness probe of cited URLs (opt-in; NOT part of the offline gate)")
    args = ap.parse_args()

    try:
        with open(args.path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"compliance_pass: 0\nerror: cannot read {args.path}: {exc}", file=sys.stderr)
        sys.exit(2)

    is_html = args.path.lower().endswith((".html", ".htm"))
    if is_html:
        violations, gates = analyze_html(text), {}
    else:
        violations, gates = analyze(text)

    link_notes = []
    link_effective = None
    if args.check_links and not is_html:  # link-check applies to markdown reports, not the HTML view
        lc = check_links_live(text)
        for url, code in lc["dead"]:
            violations.append(f"cited source is dead (HTTP {code}): {url} — LAW 0 live-link discipline")
        for url in lc["nxdomain"]:
            violations.append(f"cited source domain does not resolve (NXDOMAIN): {url} — likely fabricated or dead (LAW 0)")
        for url, why in lc["suspect"]:
            link_notes.append(f"SUSPECT ({why}; a 200 is not proof the cited content exists — verify): {url}")
        for url, why in lc["unverified"]:
            link_notes.append(f"unverified ({why}, not counted against the gate): {url}")
        if lc["skipped"]:
            link_notes.append(f"link check truncated: {lc['skipped']} URL(s) beyond the limit/time budget were not probed")
        # Inert-probe warning: if every reachable answer was 'unverified', the probe confirmed nothing.
        link_effective = bool(lc["probed"]) and (lc["probed"] - len(lc["unverified"])) > 0
        if lc["probed"] and not link_effective:
            print("WARNING: --check-links was INERT — no cited URL could be reached "
                  "(offline / proxy / network policy). Liveness is UNVERIFIED, not confirmed.", file=sys.stderr)
    violations = list(dict.fromkeys(violations))
    passed = not violations

    payload = {"path": args.path, "passed": passed, "violations": violations, "gates_found": sorted(gates.keys())}
    if args.check_links and not is_html:
        payload["link_notes"] = link_notes
        payload["link_check_effective"] = link_effective
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        if passed:
            print("OK — compliance gate passed")
        else:
            print("FAIL — compliance gate violations:")
            for v in violations:
                print(f"  - {v}")
        for n in link_notes:
            print(f"  · {n}")
    print(f"compliance_pass: {1 if passed else 0}")
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()

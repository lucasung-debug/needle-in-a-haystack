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
import sys

REQUIRED_GATES = ["FRAME", "ABDUCT", "FALSIFY", "INDEP", "C", "L1", "L2", "L3", "L4", "COST", "NULL", "FINAL"]
# Gates whose only acceptable resolved verdict is PASS:
PASS_ONLY = ["FRAME", "ABDUCT", "FALSIFY", "INDEP", "C", "L1", "L2", "L3", "L4"]

GATE_LINE = re.compile(r"^\[([A-Z0-9]+)\]\s*:\s*(.*)$")
BRACKET = re.compile(r"\[([^\]]*)\]")
URL = re.compile(r"https?://[^\s)>\]]+", re.I)
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

    # 6b. Falsification discipline: a needle FOUND (not a null result) marked [FALSIFY]=PASS must record
    #     what it ruled out. Confirmation with no recorded disconfirmation is the over-association failure
    #     mode; an honest NEEDLE NOT FOUND ([NULL]=PASS) is exempt.
    falsify_pass = gates.get("FALSIFY", {}).get("verdict") == "PASS"
    null_pass = gates.get("NULL", {}).get("verdict") == "PASS"
    considered_alternatives = bool(re.search(r"ruled[ -]?out|contradict|rejected|refuted|disprov", low))
    if final_valid and falsify_pass and not null_pass and not considered_alternatives:
        violations.append("[FALSIFY]=PASS but no ruled-out alternative or contrary evidence is recorded — confirmation, not falsification (ABDUCT holds >=2 candidates; FALSIFY must break the leader)")

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

    # de-duplicate while preserving order
    violations = list(dict.fromkeys(violations))
    return violations, gates


def main():
    ap = argparse.ArgumentParser(description="Compliance gate for needle-in-a-haystack outputs.")
    ap.add_argument("path", help="path to a finished research output (markdown)")
    ap.add_argument("--json", action="store_true", help="emit JSON report")
    args = ap.parse_args()

    try:
        with open(args.path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"compliance_pass: 0\nerror: cannot read {args.path}: {exc}", file=sys.stderr)
        sys.exit(2)

    violations, gates = analyze(text)
    passed = not violations

    if args.json:
        print(json.dumps({
            "path": args.path,
            "passed": passed,
            "violations": violations,
            "gates_found": sorted(gates.keys()),
        }, ensure_ascii=False, indent=2))
    else:
        if passed:
            print("OK — compliance gate passed")
        else:
            print("FAIL — compliance gate violations:")
            for v in violations:
                print(f"  - {v}")
    print(f"compliance_pass: {1 if passed else 0}")
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()

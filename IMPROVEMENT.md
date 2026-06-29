# IMPROVEMENT.md — PDCA log for needle-in-a-haystack

The skill should cover **more fields**, grow **heavier on purpose**, get **more refined / detailed**,
**raise the trust** of its results, and **stabilize** — measurably, one PDCA cycle at a time. This file is
the loop that makes that repeatable instead of ad hoc.

## The loop (every cycle)

**PLAN → DO → CHECK → ACT**

- **PLAN** — take the top backlog item. Name the *metric* it moves and the *check* that will prove it.
- **DO** — the smallest change that moves the metric. (ponytail still applies: shortest diff that works.)
- **CHECK** — both gates must stay green:
  - `python eval/runner.py` → `detection == 1.0` **and** `false_positive_rate == 0`.
  - skill-enhancer audit → `score 100`, `0 HARD`, `0 WARN`.
  - A new **trust check** ⇒ add ≥1 adversarial fixture that fails without it **and** confirm the honest
    fixtures still pass. **Raise the bar by adding fixtures, never by editing the judge** —
    `eval/runner.py`, `eval/expected.json`, and the existing `eval/fixtures/` are frozen.
  - A new **trust check** also gets an adversarial **red-team** before shipping (generate diverse *honest*
    outputs → must NOT be flagged; diverse *bad* outputs → must be caught). A check the red-team shows is
    high-false-positive or trivially bypassable does **not** belong in the deterministic gate — reassign it to
    the skeptic-judge. (Cycle 2 lesson.)
- **ACT** — green ⇒ commit, append a cycle entry below, promote the next backlog item. Red ⇒ revert/adjust.
- **Apply-boundary** (change class decides autonomy): reference `*.md` doc edits self-apply within a cycle;
  changes to judge-adjacent code (`scripts/`, gate logic), `templates/`, or fixtures ship only behind the two
  green gates, and any edit to `compliance_check.py` must leave ≥1 new adversarial fixture. Never weaken a gate to
  pass — add fixtures. User-facing behavior changes get surfaced, not silently shipped.

## Dashboard

| Metric | Vector | Baseline | Now |
|---|---|---|---|
| detection rate | trust · stability | 1.00 (8/8) | 1.00 (11/11) |
| false-positive rate | trust | 0.00 (0/2) | 0.00 (0/3) |
| compliance checks | trust | 13 | 16 |
| eval fixtures | stability | 10 | 14 |
| source-catalog domains | coverage | 6 | 10 |
| skill-enhancer audit | quality | 100 | 100 |
| FALSIFY failure modes (skeptic-judge) | trust | 0 | 7, per-claim (red-team 11/11 · 6/6) |
| report formats | refinement | 1 (md) | 2 (md + html) |
| CI regression guard | stability | none | GitHub Actions (eval on push/PR) |

## Backlog (ranked; move the top item each cycle)

Done: ✓ unsourced-but-VALID gap (Cycle 1) · ✓ negative-evidence / falsification discipline (Cycle 2).
Items below are seeded from the 2026-06-22 analysis of five reference skills (storm-research, bizplan,
news-for-beginner, im-designer, im-human).

- **✓ Trust — skeptic-scorecard FALSIFY (done Cycle 3)** — `references/falsify-skeptic.md` +
  `templates/skeptic-scorecard.snippet.md`: author ≠ reviewer skeptic across 7 named failure modes with a
  PASS/REWORK scorecard gating `[FALSIFY]=PASS`. Red-teamed 11/11 (fixed all 6 Cycle-2 misses). Absorbed "was
  falsification *recorded*?" from Cycle 2's reverted regex — a judge reads substance a keyword cannot.
- **Refinement — self-contained HTML report skeleton** (im-designer `visualization.md`; storm zero-dep build):
  add `templates/report.html` (inline CSS, CSS-variable theme, system fonts) + option-compare rules for competing
  hypotheses (2–3 options, vary one variable, mark the recommendation). Closes our visualization gap.
- **Trust — confirmed vs. unconfirmed report section + no-hedge rule** (im-human): a VALID report must separate
  what the sources support from open unknowns; ban hedge words ("아마 / probably / roughly") — with a fixture.
- **Coverage — source-recipe format** (news-for-beginner `site-collection-recipes.md`): a recipe per tricky source
  (boundary / why-generic-fails / working-path / fallback / pitfalls); plus more `sources.md` domains
  (real-estate, shipping & trade, environmental/standards), `methodology.md` domains, paradigms — web-verified.
- **Refinement** — deepen a reference only where a phase repeatedly runs short; never scaffold ahead of need.
- **Stability** — ≥2 adversarial fixtures per check; wire `eval/runner.py` into a SessionStart hook so the gate
  runs on every web session.

## Next directions (goals)

Standing plan; the top item moves each cycle.
- **✓ Cycle 7 — HTML self-containment gate** (closes Cycle 4's deferred gap): `compliance_check.py` validates an
  HTML report has no external resource (`<link>`/`<script src>`/`<img>`/`@import`/`url()`) and no leftover `{{ }}`;
  fixtures `good-report-html`, `bad-report-html-external`.
- **✓ Cycle 8 — NEEDLE-NOT-FOUND ↔ [NULL] consistency gate**: a headline declaring no needle while `[NULL]=NA`
  (NA = a needle was found) is flagged; fixture `bad-nnf-contradiction`.
- **✓ Cycle 9 — eval into CI**: GitHub Actions (`.github/workflows/eval.yml`) runs `eval/runner.py` on every
  push/PR (stability) — a true regression guard, stdlib-only.
- **✓ Cycle 10 — per-claim corroboration**: skeptic-judge mode 2 now scores EACH load-bearing claim's
  independent-source count (weakest wins), not just the headline.
- **Coverage**: keep adding verified, free-first source domains + recipes as questions demand them.

**Dogfood-derived backlog** (real cuts surfaced by running the skill end-to-end on a live CBDC question, 2026-06-29; ranked by trust value):
- **Cycle 11 — link liveness** (opt-in `--check-links`): the gate claimed `[L1] live` but verified nothing.
- **Cycle 12 — bind the skeptic scorecard to the gate** (`[SKEPTIC]` structural presence/PASS): the judge verdict floated free of the report.
- **Cycle 13 — retrieval-timestamp helper**: timestamps were hand-written (friction + fabrication temptation).
- **Cycle 14 — lite-mode trigger**: full FRAME is heavy for a quick "is this true?" check.
- **Cycle 15 — primary-over-secondary nudge**: a blog was cited for an EO instead of the Federal Register primary.

This campaign runs as a self-paced `/loop`: each cycle is checked by subagents (ultracode) — a plan-vs-research
**adequacy critic** plus an adversarial **red-team** — before it ships. ≥5 cycles.

**Hardening campaign:** every new deterministic check earns an adversarial red-team (FP + bypass). This round runs
five — RT1 HTML gate · RT2 NNF gate · RT3 deeper skeptic-judge · RT4 whole-gate sweep · RT5 end-to-end — recorded
per cycle below.

## Cycle log

### Cycle 1 — 2026-06-22 — Trust: the unsourced-but-VALID gap
- **PLAN** — a `[C]=PASS` + `[FINAL] VALID` output with no URL anywhere in it passed the gate clean (false
  negative): it *claims* every claim maps to a live source yet ships zero links. Close it.
- **DO** — new check in `compliance_check.py` (`[C]=PASS` + valid + no URL ⇒ violation); new adversarial
  fixture `bad-unsourced-claim`. Reused the existing `c_pass`/`final_valid` signals (no new parsing).
- **CHECK** — detection 1.00 (9/9), FP 0.00 (0/2), audit 100 / 0 HARD / 0 WARN. ✓
- **ACT** — committed. Next: per-claim corroboration check.

### Cycle 2 — 2026-06-22 — Trust: falsification discipline (attempted → reverted)
- **PLAN** — flag a needle-FOUND `[FALSIFY]=PASS` + VALID output that records no ruled-out alternative
  (the over-association failure mode from storm-research's peer-review / bizplan's negative-evidence `stance`).
- **DO** — added a deterministic check (valid + `[FALSIFY]=PASS` + `[NULL]≠PASS` + no
  `ruled-out|contradict|rejected|refuted|disprov` marker ⇒ violation) + fixture `bad-no-falsification`.
- **CHECK** — eval/audit went green, but the adversarial **red-team** (10 cases vs the live checker) exposed the
  check as brittle BOTH ways: **3/6 honest reports false-positived** (they phrased disconfirmation as "discarded /
  excluded / inconsistent with / disputes" — synonyms the regex misses) and **3/3 confirmation-only reports
  bypassed it** (a stray "…does not contradict…", "PR rejected by CI", or "not disproved" satisfied the keyword).
  Whether falsification was genuinely *recorded* is a **semantic** property a regex cannot judge; a 50%-FP hard
  gate would *lower* trust, not raise it.
- **ACT** — **reverted** the check, fixture, and dashboard (net deterministic delta this cycle: 0). Reassigned
  falsification-recording to the skeptic-scorecard cycle. The loop did its job — the red-team stopped a brittle
  gate from shipping — so the **red-team step is now a permanent part of CHECK**. The report template keeps the
  Ruled-out section as a quality cue.

### Cycle 3 — 2026-06-22 — Trust: skeptic-judge for FALSIFY
- **PLAN** — give FALSIFY the *substance-reading* review Cycle 2's regex couldn't: an **author ≠ reviewer skeptic**
  across seven named failure modes (confirmation-only · single-source/laundering · over-association · source-bias ·
  stale/retracted · sycophancy · scope) with a PASS/REWORK scorecard gating `[FALSIFY]=PASS`.
- **DO** — added `references/falsify-skeptic.md` + `templates/skeptic-scorecard.snippet.md`; wired into `research.md`
  (Phase 4/5 + v0.9), `SKILL.md` (routing + Run step 6 + templates), `_index.md`. **No new deterministic regex**
  (Cycle 2 lesson) — the judge is semantic; its check is the red-team. eval 9/9, audit 100/0/0 unchanged.
- **CHECK** — adversarial **red-team: 11/11 correct**. honest→PASS **4/4** (all 3 Cycle-2 false-positives now PASS —
  the synonym reports the regex wrongly blocked); bad→REWORK **7/7** (all 3 Cycle-2 bypasses now caught — the judge
  named the planted lexeme a "decoy with no substance" and scored modes 1+2 fatal), plus over-association→mode 3,
  source-bias→mode 4, sycophancy→mode 6, single-source→mode 2. **Cycle-2 cases fixed 6/6**; all 7 failure modes
  exercised. eval 9/9, audit 100/0/0.
- **ACT** — shipped. The judge corrects the Cycle-2 regex *both ways* — exactly the semantic read a keyword cannot do.
  Next: visualization (zero-dep HTML report skeleton, im-designer pattern), or per-claim "confirmed vs unconfirmed".

### Cycle 4 — 2026-06-22 — Refinement: self-contained HTML report view (goal item A)
- **PLAN** — findings shipped as markdown only; no shareable visual layer. Add a zero-dep HTML view (im-designer's
  token-themed self-contained skeleton + option-compare rules).
- **DO** — `templates/report.html`: self-contained (inline CSS, system fonts, **no external resources** — only `<a>`
  links to cited sources), theme entirely in `:root`, option-compare cards for competing hypotheses (exactly one
  marked recommended), a confidence badge, a confirmed-vs-unconfirmed split, and the compliance block + skeptic
  verdict. Wired into REPORT (optional) + the templates list.
- **CHECK** — audit 100/0/0; eval 9/9 (unchanged — the markdown stays the gated artifact). *Deliberate skip:* no
  deterministic HTML validator yet (the `.md` is what the gate reads; the template header encodes the self-contained
  rule). Add an HTML structural check (no external `src`/stylesheet, no leftover `{{ }}`) when HTML becomes a
  primary, gated output — logged here so the gap isn't silent.
- **ACT** — shipped.

### Cycle 5 — 2026-06-22 — Trust · readability: confirmed-vs-unconfirmed + no hedging (goal item B)
- **PLAN** — reports blurred what's *established* with what's *guessed*, and hedge words ("probably", "아마") let an
  unsupported claim read as supported (im-human's failure mode).
- **DO** — `templates/report.template.md` gains a **Confirmed vs. unconfirmed** section + a header rule: write
  "cannot confirm / 확인할 수 없습니다" over a hedge. Added a MUST-DO bullet in `SKILL.md`; `report.html` already
  carries the split.
- **CHECK** — audit 100/0/0, eval 9/9. *Deliberate skip:* no hedge-word *gate* — a keyword ban would repeat Cycle 2's
  brittleness (legit "probably" in a quoted source = false positive; synonyms = bypass). This is template + discipline,
  judged in review, not by regex.
- **ACT** — shipped.

### Cycle 6 — 2026-06-22 — Coverage: more verified sources + a source-recipe format (goal item C)
- **PLAN** — broaden reach into climate/energy + entity-identity, and capture *how* to crack a tricky source so it
  isn't relearned each run.
- **DO** — web-verified, free-first additions: **Open-Meteo** (keyless, ERA5 reanalysis from 1940) + **NOAA NCEI CDO**
  (free token) in §9; **US EIA** (free key) in §4; **GLEIF LEI** (keyless) in §8 — env vars synced to `.env.example`.
  Added a **Source-recipe** format to §0 (boundary · generic-fails · working · fallback · pitfall) with a worked
  SEC-EDGAR example (news-for-beginner pattern).
- **CHECK** — audit 100/0/0, eval 9/9. Every new source verified live against its official docs (LAW 0).
- **ACT** — shipped. Goal items A·B·C all delivered.

### Cycle 7 — 2026-06-22 — Refinement · trust: HTML self-containment gate
- **PLAN** — Cycle 4 shipped `report.html` but deferred its validator. Close the gap with a *structural* check
  (the robust kind, unlike Cycle 2's semantic regex).
- **DO** — `compliance_check.py` gains an HTML mode (routed by extension): flags external `<link>` stylesheet,
  `<script src>`, non-`data:` `<img>`, `@import`, `url(...)` to an external/protocol-relative target, leftover
  `{{ }}`, fabrication smells, and a malformed doc. `runner.py` now also picks up `report.html` fixtures; added
  `good-report-html` + `bad-report-html-external`.
- **CHECK** — eval 11/11, FP 0/3, audit 100/0/0. **RT1 7/7**: external-dep bypasses (protocol-relative `//`,
  `@import`, uppercase/spaced `<IMG SRC=>`) all caught; `data:` URIs, `url(#grad)`, and `<a href>` source links
  correctly NOT flagged.
- **ACT** — shipped. RT1 also surfaced a *latent gap*: the HTML path is self-containment-only and does not
  re-enforce LAW 0 (an `.html` could ship with fabricated/dead/undated sources — the `.html` extension is the
  cheapest dodge of the strict gate). **Closed by discipline, not duplication:** the markdown is the authoritative
  gated artifact; render HTML *from* a gate-passing `report.md`. Documented in `report.html`, `analyze_html`, and
  `research.md`.

### Cycle 8 — 2026-06-22 — Trust: NEEDLE-NOT-FOUND ↔ [NULL] consistency
- **PLAN** — a report whose headline says "NEEDLE NOT FOUND" yet marks `[NULL]=NA` is self-contradictory (NA means
  a needle was found). Catch it structurally.
- **DO** — `compliance_check.py` §8: if a heading/Answer line declares NEEDLE NOT FOUND / UNANSWERABLE while
  `[NULL]=NA` and FINAL is VALID → violation. Targets only the headline/Answer line (not prose or the NULL gate
  line) to stay false-positive-free; fixture `bad-nnf-contradiction`.
- **CHECK** — eval 11/11, FP 0/3, audit 100/0/0. **RT2 4/4**: the NNF↔`[NULL]=NA` contradiction was caught
  (including the "UNANSWERABLE" phrasing); a found-needle report mentioning "needle not found" only in *prose* was
  correctly NOT false-positived.
- **ACT** — shipped.

### Cycle 11 — 2026-06-29 — Trust: opt-in link-liveness (dogfood cut #1)
- **PLAN** — a real dogfood run (the CBDC question) showed the gate *claims* `[L1] verified live` but verifies
  nothing: a dead or fabricated URL with valid format passes. Close it without breaking the offline gate.
- **DO** — `compliance_check.py --check-links` (opt-in): probes each cited URL (HEAD→GET, stdlib `urllib`); a
  definitively-gone URL (4xx/5xx, excluding 401/403/429 = access/rate) → violation; transient / TLS / proxy →
  "unverified", never fails the gate. Network-dependent, so deliberately OUTSIDE the frozen eval/CI. Default behavior
  unchanged.
- **CHECK** — ultracode verification (adequacy critic + 4-lens red-team) found the first cut **buggy**: adequacy
  verdict "adequate but evidence-thin", and the red-team confirmed **6 high** + 9 med — the probe failed *live*
  sources (5xx/405/501/400 → DEAD), let *dead* ones pass (soft-404 HTTP 200, NXDOMAIN, 403-gone), ran on the HTML
  path, swallowed trailing quotes (`href="…"` → false 404), and was a silent **no-op** under a proxy/offline (all
  "unverified", gate green = false assurance).
- **FIX (same cycle)** — redesigned `check_links_live`: **dead = only 404/410 + NXDOMAIN**; everything the probe
  can't positively kill (5xx, 401/403/405/429/451/501, TLS/proxy/timeout) → `unverified` (never fails the gate);
  a 2xx that redirected a deep path to the bare origin → `suspect`; an inert probe → loud `WARNING` +
  `link_check_effective: false`; `--check-links` is now a **no-op on HTML**; the URL regex stops at quotes; a
  wall-clock budget + truncation note bound the worst case; `--json` adds link keys only when the flag is set.
  Proved by an **offline unit test** (`tests/test_check_links.py`, mocked network → dead 2 · nxdomain 1 · suspect 1 ·
  unverified 6 · live 3), now run in CI. Default eval 11/11, audit 100/0/0. Evidence preserved:
  `eval/dogfood-cbdc-2026-06-29.md`. Wired `--check-links` into `[L1]`/REPORT (research.md + SKILL.md).
- **ACT** — committed the fix + test; **re-red-team in flight** to confirm the 6 highs are closed with no regression.

### Red-team campaign — 2026-06-22 — 5 rounds, 21/21 (goal: "반증 5회")
- **RT1 HTML gate 7/7 · RT2 NNF gate 4/4 · RT3 skeptic-judge 4/4 · RT4 whole-gate sweep 4/4 · RT5 end-to-end 2/2.**
  Zero problems. Record: `eval/redteam-campaign-5.json`.
- RT3 confirmed the skeptic-judge catches partial-falsification (mode 1), stale source (mode 5), and scope overreach
  (mode 7), and passes a strong honest report. RT4 confirmed the markdown gate still catches unresolved placeholders,
  `[FINAL] INVALID`, and the paid-without-consent interlock, with no false-positive on a clean report. RT5 confirmed
  the **two-layer defense**: a confirmation-only report that passes the *format* gate (exit 0) is still REWORKed by
  the *judge* — format and substance are checked at different layers.

### Cycle 9 — 2026-06-22 — Stability: eval in CI
- **PLAN** — the frozen judge only ran when someone remembered to; make it automatic so the gate can't silently break.
- **DO** — `.github/workflows/eval.yml`: on every push/PR, `py_compile` the scripts then run `python eval/runner.py`
  (stdlib-only, no deps). CI fails if detection ≠ 1.0 or FP ≠ 0.
- **CHECK** — `eval/runner.py` green locally (11/11, FP 0/3); the workflow is the standing guard on GitHub. First
  CI run on push: **success** (verified via the Actions API). No red-team — CI infra, not an output gate.
- **ACT** — shipped.

### Cycle 10 — 2026-06-22 — Trust: per-claim corroboration (skeptic-judge)
- **PLAN** — mode 2 only checked the *headline* needle's sources; a well-cited headline could still rest on an
  unsourced critical sub-claim. Deepen it to *every load-bearing claim*.
- **DO** — `falsify-skeptic.md`: before scoring, list the load-bearing claims (needle + the sub-claims it depends
  on); mode 2 now requires ≥2 independent live sources for EACH, scoring the weakest. Scorecard mode-2 row updated.
  A judge, not a regex (Cycle 2 lesson holds).
- **CHECK** — eval/audit unaffected (the judge is a protocol, not the deterministic gate). **RT6 6/6**: a well-cited
  headline resting on a single-sourced or unsourced critical sub-claim → REWORK; sub-claim citation laundering (two
  URLs, one origin) → REWORK; a fully-corroborated report → PASS; and crucially a non-load-bearing single-source
  *aside* → PASS — no false positive, because the judge tested *load-bearing status* rather than mere single-sourcing;
  honest NEEDLE NOT FOUND → PASS (modes 1-3 NA). Record: `eval/redteam-cycle10-per-claim.json`.
- **ACT** — shipped.

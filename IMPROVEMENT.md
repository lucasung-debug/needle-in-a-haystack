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
| detection rate | trust · stability | 1.00 (8/8) | 1.00 (9/9) |
| false-positive rate | trust | 0.00 (0/2) | 0.00 (0/2) |
| compliance checks | trust | 13 | 14 |
| eval fixtures | stability | 10 | 11 |
| source-catalog domains | coverage | 6 | 10 |
| skill-enhancer audit | quality | 100 | 100 |

## Backlog (ranked; move the top item each cycle)

Done: ✓ unsourced-but-VALID gap (Cycle 1) · ✓ negative-evidence / falsification discipline (Cycle 2).
Items below are seeded from the 2026-06-22 analysis of five reference skills (storm-research, bizplan,
news-for-beginner, im-designer, im-human).

- **Trust — skeptic-scorecard FALSIFY** (storm-research peer-review keyed to named failure modes; bizplan
  `12-verification.md` 4-persona audit): turn FALSIFY into a skeptic persona with scripted attacks + a numeric
  pass threshold; each named failure mode gets an adversarial fixture. **Now also owns "was falsification
  *recorded*?"** — reassigned from Cycle 2's reverted regex; a judge can read for substance a keyword cannot.
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

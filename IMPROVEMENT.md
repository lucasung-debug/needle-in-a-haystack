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
- **ACT** — green ⇒ commit, append a cycle entry below, promote the next backlog item. Red ⇒ revert/adjust.

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

- **Coverage** — more `sources.md` domains (real-estate/property, shipping & trade, environmental/standards);
  more `methodology.md` domains; more paradigms in `paradigm.md`. Each addition web-verified, free-first.
- **Trust** — new compliance checks, each with its own adversarial fixture:
  per-claim corroboration (≥2 independent sources where `[INDEP]`/`[C]` claim it); provenance-tag vocabulary
  (`[retrieved|inferred|assumed]` only); a `FINAL VALID` output that still says `NEEDLE NOT FOUND` in its body
  (self-contradiction).
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

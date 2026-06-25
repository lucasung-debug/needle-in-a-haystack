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
| FALSIFY failure modes (skeptic-judge) | trust | 0 | 7 (red-team 11/11) |
| report formats | refinement | 1 (md) | 2 (md + html) |

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

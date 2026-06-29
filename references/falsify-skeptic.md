# falsify-skeptic.md — the skeptic-judge for FALSIFY (Phase 4)

> Derived from `research.md`. Loaded on demand at **FALSIFY (Phase 4)** and consulted at **SELF-CORRECT (Phase 5)**.
> Purpose: turn "try to break the finding" from a vibe into an **auditable adversarial review**. A regex cannot tell
> whether falsification genuinely happened (it keys on words, not substance — see IMPROVEMENT.md Cycle 2); a skeptic
> *reading for substance* can. This judge produces the evidence on which an honest `[FALSIFY]=PASS` rests.

## Stance (author ≠ reviewer)

You did **not** write the finding. Assume the needle is **wrong** and try to break it. Default to skepticism: a
finding survives only if you *cannot* break it on the evidence present. "I couldn't break it" is the only thing that
earns `[FALSIFY]=PASS`. Be specific — every verdict cites a line/source in the output under test, never a vibe.

In **full/plan mode**, run this as a separate pass (ideally a sub-agent via `Task`, so the reviewer holds no authoring
context). In **lite mode**, run it inline but still fill the scorecard. It is reasoning only — **no paid calls, no new
sources required**; if a mode can only be cleared by fetching more, that itself is a `weak`/`fatal`, not a pass.

Before scoring, **list the load-bearing claims** — the needle *plus every sub-claim it depends on* — and apply the
corroboration test (mode 2) to **each one**, not just the headline. A well-cited headline resting on an unsourced
critical sub-claim has not survived falsification.

## The seven attacks (named failure modes)

Score each: **clear** (attack fails, finding holds) · **weak** (a real soft spot — disclose it in Limits) · **fatal**
(the finding does not survive this attack as stated).

1. **Confirmation-only** — Was a *competing* candidate genuinely broken, or was only the leader confirmed? ABDUCT must
   have held ≥2 candidates; FALSIFY must show ≥1 of them *failing a prediction*. No broken alternative ⇒ `fatal`.
2. **Single-source / citation laundering (per load-bearing claim)** — Does **each** load-bearing claim rest on
   **≥2 independent live sources**? One source — or one source recited under different URLs/outlets that trace to the
   same origin — ⇒ `fatal` (or `weak` if that source is a primary authority and the claim is narrow). Score the
   *weakest* load-bearing claim: a fully-sourced needle with one unsourced critical sub-claim is still `fatal`.
3. **Over-association / evidence-inflation** — Is correlation / co-occurrence / name-match sold as **cause or identity**?
   Mechanism asserted without a mechanism shown ⇒ `weak`→`fatal` by how load-bearing it is. **Also grade the evidence:**
   a load-bearing claim stated as *established* but supported only at **E3/E4** (single self-report / survey / vendor /
   anecdote) is `weak`→`fatal` — don't launder marketing or a lone survey into proof; scope the claim to its grade.
4. **Source-bias transfer** — Do the sources share one origin, vendor, or agenda, so the finding just inherits their
   bias? No independent or *adversarial* source consulted ⇒ `weak`→`fatal`. Citing only *secondary* commentary for a
   fact that has a reachable *primary* source (official text/dataset/ruling) is `weak` — fetch and cite the primary.
5. **Stale / retracted / superseded** — Is the newest authoritative source checked? Is any cited source retracted,
   deprecated, or superseded by a later version? Unchecked recency on a time-sensitive claim ⇒ `weak`→`fatal`.
6. **Sycophancy / premise-adoption** — Does the finding mirror the asker's expectation or smuggle in their premise
   rather than follow the evidence (`[INDEP]`)? Evidence reads as reverse-engineered to the wanted answer ⇒ `fatal`.
7. **Scope overreach** — Is the claim wider (population, time, domain, certainty) than the evidence supports? Trim the
   claim to the evidence, or `weak`→`fatal`.

## Verdict (the gate on `[FALSIFY]`)

- **PASS** — *zero* `fatal`, **and** the leader survived ≥1 explicit disconfirmation attempt, **and** ≥2 independent
  live sources (LAW 0). Any `weak` must be written into the report's **Limits / What would change the answer**.
- **REWORK `<mode#>`** — one or more `fatal`: loop back (Phase 1 reframe or Phase 3 collect), fix that specific mode,
  re-judge. Never mark `[FALSIFY]=PASS` to move on.
- **NEEDLE NOT FOUND** — if no candidate can be made to survive, that is the correct terminal state (LAW: never
  fabricate a survivor). An honest null result is judged on modes 4–6 only; 1–3 (which need a positive needle) are `NA`.

Record the verdict in `templates/skeptic-scorecard.snippet.md` and keep it with the output, **and carry the PASS/REWORK
result into the compliance block as `[SKEPTIC]`** — the deterministic gate requires `[SKEPTIC]=PASS` for any shipped
needle, so the judge's verdict is auditable and cannot float free. An `[FALSIFY]=PASS` whose scorecard is missing,
unresolved, or itself `REWORK` is not an honest pass.

## Why this is a judge, not a regex

Cycle 2 tried to detect "falsification recorded" with a keyword search. A red-team broke it both ways: honest reports
phrased disconfirmation as *discarded / excluded / inconsistent with / disputes* (the regex missed them — false
positives), and confirmation-only reports planted a stray *"does not contradict"* to pass (bypass). Substance is not a
lexeme. This judge reads for the **broken alternative and the independent corroboration**, which is what FALSIFY means.

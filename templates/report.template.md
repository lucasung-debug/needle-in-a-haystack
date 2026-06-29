<!-- REPORT skeleton (research.md REPORT phase). Fill {{...}}; keep the section order and
     the compliance block. Tag every claim [retrieved | inferred | assumed] and keep observed
     data visually separate from interpretation. Gate with scripts/compliance_check.py.
     A "needle found" output should keep a real, non-empty Ruled-out candidates / contrary-evidence entry —
     recorded falsification is a quality requirement (assessed in review, not by the format gate).
     Separate confirmed from unconfirmed; for anything unconfirmed, write "cannot confirm / 확인할 수 없습니다"
     rather than hedging ("probably", "maybe", "I think", "아마", "대충") — state what the evidence supports, flag the rest.
     Stamp each source's retrieval time with scripts/now.py (ISO-8601 UTC) — never hand-type it.
     Audience modes: the human-facing BRIEF leads with the answer + Confidence + what-to-do, in plain language (no
     [SKEPTIC]/LAW-0 jargon); the compliance block is an AUDIT appendix, not the headline. The gated artifact is always
     this full markdown — gate it, then present the brief. -->

# BLUF — {{one-line answer, or "NEEDLE NOT FOUND / UNANSWERABLE"}}

**Answer:** {{the finding, stated at claim-strength ≤ evidence-strength}} `[retrieved | inferred]`
**Confidence:** {{high | medium | low}} — {{one plain-language reason a non-expert can act on}}

## Key sources
- {{url}} — {{what it supports}} — {{live|dead|throttled|paywalled}}, retrieved {{YYYY-MM-DDThh:mm:ssZ}} `[retrieved]`
- {{url}} — {{…}} — retrieved {{YYYY-MM-DDThh:mm:ssZ}} `[retrieved]`

## Ruled-out candidates
- {{candidate}} — {{why it failed falsification}} `[inferred]`

## Conflicts / gaps
- {{conflicting source or open gap, flagged not silently resolved}}

## Confirmed vs. unconfirmed (evidence-graded)
Grade each load-bearing claim — **E1** controlled (RCT / experiment / systematic review) · **E2** corroborated (≥2 independent primary/observational sources agree) · **E3** single / self-report (one source, or a survey self-report) · **E4** vendor / anecdote (marketing or unverified). State the claim no stronger than its grade.
- **Confirmed** (E1–E2): {{claim}} `[retrieved · E1|E2]`
- **Unconfirmed / treat as a claim** (E3–E4 — write "cannot confirm", never present as proven): {{item}} `[assumed · E3|E4]`

## What would change the answer
- {{the evidence that would overturn this}}

## Limits
- {{scope boundary; confidence: low | medium | high}}

## Audit trail (appendix — for verification, not the headline reader)
{{paste templates/compliance-block.snippet.md here, with every verdict resolved}}

<!-- REPORT skeleton (research.md REPORT phase). Fill {{...}}; keep the section order and
     the compliance block. Tag every claim [retrieved | inferred | assumed] and keep observed
     data visually separate from interpretation. Gate with scripts/compliance_check.py.
     A "needle found" output should keep a real, non-empty Ruled-out candidates / contrary-evidence entry —
     recorded falsification is a quality requirement (assessed in review, not by the format gate).
     Separate confirmed from unconfirmed; for anything unconfirmed, write "cannot confirm / 확인할 수 없습니다"
     rather than hedging ("probably", "maybe", "I think", "아마", "대충") — state what the evidence supports, flag the rest. -->

# BLUF — {{one-line answer, or "NEEDLE NOT FOUND / UNANSWERABLE"}}

**Answer:** {{the finding, stated at claim-strength ≤ evidence-strength}} `[retrieved | inferred]`

## Key sources
- {{url}} — {{what it supports}} — {{live|dead|throttled|paywalled}}, retrieved {{YYYY-MM-DDThh:mm:ssZ}} `[retrieved]`
- {{url}} — {{…}} — retrieved {{YYYY-MM-DDThh:mm:ssZ}} `[retrieved]`

## Ruled-out candidates
- {{candidate}} — {{why it failed falsification}} `[inferred]`

## Conflicts / gaps
- {{conflicting source or open gap, flagged not silently resolved}}

## Confirmed vs. unconfirmed
- **Confirmed** (retrieved + corroborated by ≥2 independent sources): {{claim}} `[retrieved]`
- **Unconfirmed / unknown** (write "cannot confirm", never a hedge): {{open item}} `[assumed]`

## What would change the answer
- {{the evidence that would overturn this}}

## Limits
- {{scope boundary; confidence: low | medium | high}}

{{paste templates/compliance-block.snippet.md here, with every verdict resolved}}

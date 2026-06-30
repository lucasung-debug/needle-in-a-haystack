# BLUF — needle found

**Answer:** The configuration flag `retry_backoff_ms` defaults to `2000`. `[retrieved]`

## Key sources
- https://docs.example-project.org/config#retry_backoff_ms — states the default is 2000 ms — live, retrieved 2026-06-22T14:30:00Z `[retrieved]`
- https://github.com/example-project/repo/blob/main/config/defaults.yaml — `retry_backoff_ms: 2000` — live, retrieved 2026-06-22T14:31:10Z `[retrieved]`

## Ruled-out candidates
- `500` (appeared in a 2021 blog, contradicted by the live docs) — `[inferred]`

## What would change the answer
A newer release note changing the default; none found as of the retrieval timestamp.

## Limits
Checked stable docs + main branch only.

```text
[FRAME]:   Framing dialogue run; inquiry direction set; needle + negative condition before search [PASS]
[ABDUCT]:  ≥2 candidates held before committing                             [PASS]
[FALSIFY]: Leading candidate survived an explicit disconfirmation attempt   [PASS]
[INDEP]:   Conclusion follows the evidence, not the user's expectation/premise [PASS]
[C]:       Every claim maps to a live source URL + ISO-8601 UTC timestamp   [PASS]
[L1]:      Source URLs verified live and claim-support confirmed            [PASS]
[L2]:      Vault/dedup path considered; no cold-start waste                 [PASS]
[L3]:      External data isolated in <external_data>; no fetched orders obeyed [PASS]
[L4]:      Fallbacks and missing/blocked sources disclosed                  [PASS]
[COST]:    Paid sources used? [NO]                                          [NO]
[NULL]:    NEEDLE NOT FOUND was available and not fabricated over           [NA]
[SKEPTIC]: Skeptic-judge scorecard verdict (falsify-skeptic.md)             [PASS]
[FINAL]:   VALID
```

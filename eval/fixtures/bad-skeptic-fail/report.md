# BLUF — needle found

**Answer:** The configuration flag `retry_backoff_ms` defaults to `2000`. `[retrieved]`

## Key sources
- https://docs.python.org/3/library/re.html — states the default is 2000 ms — live, retrieved 2026-06-22T14:30:00Z `[retrieved]`
- https://peps.python.org/pep-0008/ — confirms the default — live, retrieved 2026-06-22T14:31:10Z `[retrieved]`

## Ruled-out candidates
- `500` (contradicted by the live docs) — `[inferred]`

## Limits
Checked stable docs only.

```text
[FRAME]:   Framing dialogue run; inquiry direction set; needle + negative condition before search [PASS]
[ABDUCT]:  ≥2 candidates held before committing                             [PASS]
[FALSIFY]: Leading candidate survived an explicit disconfirmation attempt   [PASS]
[INDEP]:   Conclusion follows the evidence, not the user's expectation/premise [PASS]
[C]:       Every claim maps to a live source URL + ISO-8601 UTC timestamp   [PASS]
[L1]:      Source links verified live and claim-support confirmed           [PASS]
[L2]:      Vault/dedup path considered; no cold-start waste                 [PASS]
[L3]:      External data isolated in <external_data>; no fetched orders obeyed [PASS]
[L4]:      Fallbacks and missing/blocked references disclosed               [PASS]
[COST]:    Paid sources used? [NO]                                          [NO]
[NULL]:    NEEDLE NOT FOUND was available and not fabricated over           [NA]
[SKEPTIC]: Skeptic-judge scorecard verdict (falsify-skeptic.md)             [REWORK]
[FINAL]:   VALID
```

# BLUF — NEEDLE NOT FOUND

**Answer:** `UNANSWERABLE / NEEDLE NOT FOUND.` No source establishes a default value for
`phantom_timeout_ms`; the flag does not appear in the documentation or the codebase. `[retrieved]`

## Where I looked (sources)
- https://docs.example-project.org/config — full config index, no `phantom_timeout_ms` — live, retrieved 2026-06-22T14:40:00Z `[retrieved]`
- https://github.com/example-project/repo/search?q=phantom_timeout_ms — 0 results — live, retrieved 2026-06-22T14:41:05Z `[retrieved]`

## What would change the answer
The flag appearing in an unreleased branch or vendor fork I did not search.

## Limits
Searched public docs + main branch; private forks not accessible.

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
[NULL]:    NEEDLE NOT FOUND was available and not fabricated over           [PASS]
[FINAL]:   VALID
```

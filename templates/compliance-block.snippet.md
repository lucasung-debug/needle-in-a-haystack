<!-- Paste at the END of every research output. Replace each [PASS/FAIL] etc. with a
     resolved verdict. Then gate it: python ${CLAUDE_SKILL_DIR}/scripts/compliance_check.py <output.md>
     The script exits non-zero unless every verdict is resolved, no gate is FAIL, FINAL is
     VALID, paid use carries consent, and provenance is not fabricated. -->

```text
[FRAME]:   Framing dialogue run; inquiry direction set; needle + negative condition before search [PASS/FAIL]
[ABDUCT]:  ≥2 candidates held before committing                             [PASS/FAIL]
[FALSIFY]: Leading candidate survived an explicit disconfirmation attempt   [PASS/FAIL]
[INDEP]:   Conclusion follows the evidence, not the user's expectation/premise [PASS/FAIL]
[C]:       Every claim maps to a live source URL + ISO-8601 UTC timestamp   [PASS/FAIL]
[L1]:      Source URLs verified live and claim-support confirmed            [PASS/FAIL]
[L2]:      Vault/dedup path considered; no cold-start waste                 [PASS/FAIL]
[L3]:      External data isolated in <external_data>; no fetched orders obeyed [PASS/FAIL]
[L4]:      Fallbacks and missing/blocked sources disclosed                  [PASS/FAIL]
[COST]:    Paid sources used? [YES/NO]  If YES, explicit consent recorded [YES/NO]
[NULL]:    NEEDLE NOT FOUND was available and not fabricated over           [PASS/FAIL/NA]
[FINAL]:   VALID
```

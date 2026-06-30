<!-- skeptic-scorecard.snippet.md — fill at FALSIFY (Phase 4) per references/falsify-skeptic.md.
     Author ≠ reviewer. Every verdict cites a line/source in the output under test. Keep this with the output;
     an [FALSIFY]=PASS without a PASS scorecard is not an honest pass. Verdicts: clear | weak | fatal | NA. -->

## Skeptic scorecard (FALSIFY)

**Leader under test:** <one-line needle>

| # | Failure mode | Attack question | Verdict | One-line reason (cite line/source) |
|---|--------------|-----------------|---------|------------------------------------|
| 1 | Confirmation-only        | Was a *competing* candidate broken, not just the leader confirmed? | clear/weak/fatal/NA | |
| 2 | Single-source/laundering | ≥2 *independent* live sources behind EACH load-bearing claim (score the weakest)? | clear/weak/fatal/NA | |
| 3 | Over-association / evidence-inflation | Correlation sold as cause? An E3/E4 (self-report/vendor) claim stated as *proven*? | clear/weak/fatal/NA | |
| 4 | Source-bias transfer     | Do the sources share one origin/agenda? Any adversarial source?    | clear/weak/fatal    | |
| 5 | Stale/retracted / volatility | Newest source checked; nothing superseded? Volatile topic carries an *as-of + recheck* marker? | clear/weak/fatal | |
| 6 | Sycophancy/premise       | Does the finding mirror the asker's premise, not the evidence?     | clear/weak/fatal    | |
| 7 | Scope overreach / conditional honesty | Claim wider than evidence? A *conditional* answer faked as a single yes/no (branches hidden)? | clear/weak/fatal/NA | |

**Verdict:** `PASS` (zero fatal · leader survived ≥1 disconfirmation · ≥2 independent live sources)
| `REWORK <mode#>` (loop to Phase 1/3, fix, re-judge) | `NEEDLE NOT FOUND`

**Weak spots carried into Limits:** <list any `weak` rows, or "none">

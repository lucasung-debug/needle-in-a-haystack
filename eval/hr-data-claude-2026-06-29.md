<!-- WORKED EXAMPLE #2 — a CONDITIONAL + VOLATILE answer (dogfood #3, 2026-06-29). Complements the single-needle
     example (hr-ai-research-2026-06-29.md). Demonstrates Cut 1 ("If it depends — find your case" branches) and
     Cut 2 (an "As of" / recheck stamp on a fast-changing subject). Gate-passing:
     `python scripts/compliance_check.py eval/hr-data-claude-2026-06-29.md` → exits 0. -->

# BLUF — needle found (conditional)

**Answer:** **It depends on which Claude you use — find your case below.** The short version: never put employee
personal data into a *consumer* chatbot; it's defensible on a *commercial* tier with the right contract, but the
vendor tier alone does not make you legally compliant. `[retrieved]`
**Confidence:** high on the consumer-vs-commercial split.
**As of:** 2026-06-29 — recheck at privacy.claude.com before relying; these terms changed in Aug 2025 and again Jun 2026.

## If it depends — find your case
| Your situation | Answer | What to do |
|---|---|---|
| Free / Pro / Max Claude (or free ChatGPT) | ❌ No | Don't paste employee data; move to a commercial tier |
| Claude for Work / Enterprise / API + DPA | ⚠️ Defensible (data axis) | Turn on Zero-Data-Retention; minimize/anonymize |
| EU employees' data (any tier) | ➕ Extra steps required | DPIA + lawful basis + tell employees; human owns decisions |
| Special-category data (health, religion…) | ⛔ Default no | Needs an explicit Art. 9 basis or don't |

## Key sources
- https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training — Anthropic: commercial/API not used for training by default — **primary** — live, retrieved 2026-06-29T02:10:00Z `[retrieved · E1]`
- https://www.anthropic.com/news/updates-to-our-consumer-terms — Anthropic: consumer Free/Pro/Max train-unless-opt-out (2025-08-28), up to 5-yr retention — **primary** — live, retrieved 2026-06-29T02:11:00Z `[retrieved · E1]`
- https://iapp.org/news/a/data-protection-issues-for-employers-to-consider-when-using-generative-ai — IAPP: employer GenAI duties (DPIA, lawful basis, oversight) — live, retrieved 2026-06-29T02:13:00Z `[retrieved · E2]`
- https://humanfirewall.io/case-study-on-samsungs-chatgpt-incident/ — Samsung (2023): staff leaked confidential data via a consumer chatbot — live, retrieved 2026-06-29T02:14:00Z `[retrieved · E2]`

## Ruled-out candidates
- "Yes, chatbots are fine for employee data" — ruled out (consumer tiers train on it; commercial still needs GDPR work). `[inferred]`
- "No, never under any setup" — ruled out (commercial + DPA + GDPR compliance is a defensible path). `[inferred]`

## Confirmed vs. unconfirmed (evidence-graded)
- **Confirmed (E1–E2)**: consumer tiers may train on chats unless opted out `[E1]`; commercial/API not trained on by default + ZDR available `[E1]`; GDPR adds DPIA/lawful-basis/oversight duties `[E2]`.
- **Unconfirmed — get your DPO/counsel**: whether *your specific* contract + config is compliant in *your* jurisdiction. Cannot confirm generically. `[assumed]`

## What would change the answer
A vendor terms change (frequent) or new EU AI Act / GDPR enforcement — recheck the vendor privacy center.

## Limits
As-of 2026-06-29; vendor terms are volatile. Not legal advice — confirm with your DPO/counsel.

## Audit trail (appendix — for verification, not the headline reader)
```text
[FRAME]:   Framing run; conditional + volatile question detected; negative condition set before search  [PASS]
[ABDUCT]:  ≥2 candidates held (yes / no / conditional) before committing                                [PASS]
[FALSIFY]: "Simple yes/no" attacked; needle scoped to the conditional branches that survived            [PASS]
[INDEP]:   Follows the terms + law, not a pro-adoption or anti-AI premise                                [PASS]
[C]:       Every claim maps to a live source URL + ISO-8601 UTC timestamp                                [PASS]
[L1]:      Source URLs verified live and claim-support confirmed                                         [PASS]
[L2]:      No vault dedup needed                                                                         [PASS]
[L3]:      External data isolated; no fetched instructions obeyed                                        [PASS]
[L4]:      Volatility disclosed (As-of date + recheck note)                                              [PASS]
[COST]:    Paid sources used? [NO]                                                                       [NO]
[NULL]:    NEEDLE NOT FOUND was available and not fabricated over                                        [NA]
[SKEPTIC]: 7 modes attacked; primary vendor terms (not blogs); conditional branches shown not faked; as-of/recheck stamped [PASS]
[FINAL]:   VALID
```

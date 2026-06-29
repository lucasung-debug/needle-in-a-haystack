<!-- WORKED EXAMPLE — a complete, gate-passing needle-in-a-haystack output (dogfood #2, 2026-06-29).
     Demonstrates the skill's signature: framing-before-search, falsification scoping the needle, evidence-strength
     grading (E1–E4), confirmed-vs-unconfirmed, a non-developer brief up front, and the compliance block as an audit
     appendix. Run `python scripts/compliance_check.py eval/hr-ai-research-2026-06-29.md` → exits 0. -->

# BLUF — needle found (scoped)

**Answer:** For a non-developer HR professional, AI/Claude **reliably saves time on language-heavy, lower-stakes draft
work** — job descriptions, policies, emails, screening-assist, L&D content, onboarding FAQs, first-draft performance
summaries — with the **largest gains for less-experienced staff**. But org-level **"HR productivity ↑X%" claims are
mostly self-reported / vendor, not measured**. `[retrieved]`
**Confidence:** medium-high on the task-level wins (controlled-trial evidence); low on org-level magnitude — capture the
task-level savings now, treat "transforms HR" claims as unproven.

## Key sources
- https://www.nber.org/papers/w31161 — Brynjolfsson, Li & Raymond, "Generative AI at Work" (RCT, 5,172 agents): +14% productivity, +34% for least-experienced — **primary** — live, retrieved 2026-06-29T01:10:00Z `[retrieved · E1]`
- https://laweconcenter.org/resources/ai-productivity-and-labor-markets-a-review-of-the-empirical-evidence/ — evidence review: Noy & Zhang (writing −40% time, +0.45 SD), Copilot (+55.8%) — **secondary synthesis of primaries** — live, retrieved 2026-06-29T01:11:00Z `[retrieved · E1]`
- https://www.shrm.org/topics-tools/research/state-of-ai-hr-2026/full-report — SHRM (n≈1,722): recruiting top use case (27%); 89% in recruiting say AI saves time; only 17% "highly successful" — **survey self-report** — live, retrieved 2026-06-29T01:12:00Z `[retrieved · E3]`
- https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/generative-ai-and-the-future-of-hr — McKinsey: HR GenAI a cost-cutter (≤10%), not a revenue driver — live, retrieved 2026-06-29T01:13:00Z `[retrieved · E2]`
- https://www.gartner.com/en/newsroom/press-releases/2025-10-16-ai-in-hr-separate-hype-from-reality-to-achieve-business-goals — Gartner: ~half of AI-in-HR innovations are hype; change-management → 2.6× more likely to succeed — live, retrieved 2026-06-29T01:14:00Z `[retrieved · E2]`
- https://www.osc.ny.gov/state-agencies/audits/2025/12/02/enforcement-local-law-144-automated-employment-decision-tools — NY State Comptroller (Dec 2025): NYC Local Law 144 (AI-hiring bias-audit) enforcement is "ineffective" — **primary** — live, retrieved 2026-06-29T01:15:00Z `[retrieved · E2]`

## Ruled-out candidates / hype filtered out
- "AI transforms HR productivity org-wide (↑20–40%)" — **ruled out as unproven**: cited org-level figures are self-reported (E3) or vendor (E4); the controlled (E1) numbers are for *general* writing/support/coding, not HR org outcomes. McKinsey's measured HR impact is a ≤10% cost-cut. `[inferred]`
- "AI can own HR decisions (hiring/promotion)" — **ruled out for autonomy**: hallucination on factual/compliance content + bias/legal exposure (NYC LL144) make AI an assistant, not a decider. `[retrieved]`

## Confirmed vs. unconfirmed (evidence-graded)
Grades — **E1** controlled (RCT) · **E2** corroborated (≥2 independent) · **E3** single/self-report · **E4** vendor/anecdote. Claim ≤ grade.
- **Confirmed (E1–E2)**: task-level time savings on language/draft tasks `[E1]`; gains largest for juniors `[E1]`; recruiting is the most-adopted HR use case and success depends on change management `[E2]`.
- **Unconfirmed (E3–E4) — treat as a claim, not a fact**: specific org-level "HR productivity ↑X%" numbers `[E3 self-report]`; that AI raises decision *quality* in HR `[E4 vendor]`; ROI beyond modest cost-cutting `[E3]`. Cannot confirm.

## Playbook — Claude for HR (highest-evidence tasks first)
| HR task | How to use Claude | Guardrail (non-negotiable) |
|---|---|---|
| JD / policy / email | First draft, then plain-language rewrite | Verify every factual/legal claim against the source — never ship Claude's facts unchecked |
| Résumé screening **assist** | Summarize/map to must-haves; quote evidence | Never auto-reject; bias-audit any scoring tool (NYC LL144); human decides |
| Onboarding / HR FAQ | Answer **only** from your own docs | "If it's not in the handbook, say so" (anti-hallucination) |
| L&D content | Draft modules/quizzes | SME reviews accuracy |
| Performance reviews | First-pass synthesis of feedback | Manager owns the rating; AI never rates people |

**Two rules that make Claude trustworthy for HR:** (1) ground it on your own documents and forbid outside answers;
(2) a human owns every decision and every fact that ships — AI drafts, you verify.

## What would change the answer
A rigorous RCT measuring *HR-team* output (not general writing) would move org-level claims E3→E1; stronger LL144
enforcement would raise compliance stakes.

## Limits
Public sources as of 2026-06-29; many HR figures are survey self-reports (graded E3). Confidence: high on task-level
savings + guardrail needs; low on org-level magnitude.

## Audit trail (appendix — for verification, not the headline reader)
```text
[FRAME]:   Framing dialogue run; scope (HR overview) + negative condition set before search  [PASS]
[ABDUCT]:  ≥3 candidates held (drafting / screening / hype-skeptic) before committing        [PASS]
[FALSIFY]: Hype hypothesis (H3) actively tested; needle scoped to what survived              [PASS]
[INDEP]:   Conclusion follows the evidence, not a pro-AI or anti-AI premise                   [PASS]
[C]:       Every claim maps to a live source URL + ISO-8601 UTC timestamp                     [PASS]
[L1]:      Source URLs verified live and claim-support confirmed                              [PASS]
[L2]:      No vault dedup needed (fresh query)                                                [PASS]
[L3]:      External data isolated; no fetched instructions obeyed                             [PASS]
[L4]:      Survey-vs-RCT evidence limits disclosed (E-grades)                                 [PASS]
[COST]:    Paid sources used? [NO]                                                            [NO]
[NULL]:    NEEDLE NOT FOUND was available and not fabricated over                             [NA]
[SKEPTIC]: 7 modes attacked; over-association/evidence-inflation (org-level hype) caught and scoped out; ≥2 independent incl. a primary RCT [PASS]
[FINAL]:   VALID
```

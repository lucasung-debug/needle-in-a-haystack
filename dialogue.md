# dialogue.md — The Framing Dialogue (the staged "doubt" front-end of FRAME)

> Derived from `philosophy.md`. Runs at the **start of FRAME** in plan/full mode; compressed to one pass in lite mode.
> The output is a **framed-question object** that feeds DESIGN (`methodology.md`) and ROUTE (`sources.md`).
>
> **Method, borrowed and retargeted.** The staged-doubt procedure here is adapted from the `doubt` planning skill
> (which builds on Descartes' *Discourse on Method*) — but retargeted from *product planning* to *research framing*.
> We borrow the method, not its machinery: no reference-file tree, no pipeline, no document factory. Its arc —
> ***Dubito → Experior → Construo*** ("I doubt → I test → I build") — is exactly right for FRAME: doubt the framing,
> name the cheapest disconfirming test, then build the plan.

---

## 0. Why a dialogue at all

- **The request is a symptom, not the question.** Dewey: problems don't pre-exist inquiry; *formulating* the problem
  is the work, not a preliminary to it (`paradigm.md` ref 12). A vague request is the first thing to falsify.
- **This is where research usually fails** — fixing a topic / keyword / source on reflex before asking what is truly
  being investigated and why. The dialogue exists to stop that reflex.
- **Posture:** methodic doubt (Descartes — provisionally suspend whatever *can* be doubted, so only stable footing
  remains)[¹] crossed with Socratic *elenchus* (surface and test assumptions by drawing tensions out of the user's
  **own** answers — never import premises, never lead).[²] Constructive, not corrosive: doubt ends when a footing is
  found, not when everything is destroyed.

---

## 1. Hard rules for the dialogue

- Use **AskUserQuestion** for every interactive question. Batch related questions; offer a recommended default per question.
- Ask the **minimum** needed to pin each gate — do not interrogate. *If the dialogue grows longer than the research
  would, it has become the haystack* (`philosophy.md` §3). The Stop Rule (§4) enforces this.
- **Socratic, not leading:** questions surface the user's assumptions; they never smuggle in your preferred answer.
- **If the user is absent / async:** state explicit assumptions in place of answers, tag them `[assumed]`, and proceed.
  Never stall waiting. Surface the assumptions in the report so they can be challenged.

---

## 2. The staged protocol (each stage is a gate — don't advance until it's pinned)

| Stage | Name (borrowed) | Do | Gate to advance |
|-------|-----------------|----|-----------------|
| **0** | *Restate & doubt* (Genius Malignus) | Mirror the request back as a **falsifiable conjecture about what the user needs.** "If an evil genius framed this request to mislead me, what am I taking for granted?" List the suspended assumptions. | Request restated as a conjecture; assumptions surfaced (a handful, not exhaustive). |
| **1** | *Assumption ledger* | For each surfaced assumption record `{claim · how load-bearing (criticality) · how fragile (evidence so far) · cost to check}`. Rank. | The **Critical few** identified — assumptions that, if false, collapse the whole inquiry. These become the first falsification targets. |
| **2** | *Purpose (왜)* | What decision or action does the answer serve? Who is the audience? What is at stake, and by when? | Purpose + stakes pinned → fixes the **mode** (lite/full/plan) and the report altitude. |
| **3** | *Indubitable Question Core* (Cogito) | Strip the request to the **real need, with no premature topic / method / source words.** (As `doubt`'s Cogito forbids solution words: *"I want to regain a sense of financial control,"* not *"a budgeting app."*) | A one-sentence question core that names the **needle** by what it *is*, not by the first keyword that came to mind. |
| **4** | *Scope & unit* | Boundaries, unit of analysis, time/place, inclusion/exclusion. Separate **Justified** decisions (the question or its direction decides them) from **Taste** decisions (values, audience, scope trade-offs — the user must choose). | Scope fixed; Taste decisions put to the user, Justified ones deduced and shown. |
| **5** | *Direction (paradigm lens) & domain* | Use the **paradigm lens** (`paradigm.md` §2) not as a label to declare but as a **menu of directions** to branch the questioning — *regularity/measurement · meaning & lived experience · underlying mechanism · what-works · power & change*. Ask the one branching question that fixes direction; load the **domain** adapter (`methodology.md` §2). | Inquiry **direction** set (it steers what counts as evidence and which design fits) — no formal paradigm commitment required. |
| **6** | *Answerability + negative condition* (Experior) | Pressure-test the question: **FINER** — Feasible, Interesting, Novel, Ethical, Relevant[³]; for empirical/clinical questions shape with **PICO(T)**[⁴]. Define success criteria **and** the **negative condition** (what observation would mean `NEEDLE NOT FOUND`). Name the **cheapest disconfirming check**. | Question passes FINER; success criteria + negative condition + cheapest-disconfirmation written. |
| **7** | *Provisional direction & confirm* (Construo) | Present **≥2 candidate inquiry directions** (abduction never commits to one) + a plan sketch + the Critical assumptions to test first. Get explicit **go / redirect**. | User confirms direction (or it is `[assumed]` and stated). Only now proceed to DESIGN. |

---

## 3. The framed-question object (the FRAME deliverable → DESIGN / ROUTE)

The dialogue ends by emitting this compact block — the handoff `methodology.md` and `sources.md` consume:

```text
PURPOSE        : <decision/action it serves> · audience · stakes · deadline
QUESTION CORE  : <one sentence, no premature method/topic/source words>
SCOPE & UNIT   : <boundaries · unit of analysis · time/place · in/out>
DIRECTION      : <regularity/measurement | meaning | mechanism | what-works | power/change>  (paradigm lens; optional: name the paradigm if useful)
DOMAIN         : <social | medical | engineering | natural-science | humanities | cross>
SUCCESS        : <what counts as the needle found>
NEGATIVE COND. : <what observation = NEEDLE NOT FOUND>
CRITICAL ASSUMPTIONS : <the few that, if false, collapse the inquiry — test first>
DIRECTIONS     : <≥2 provisional candidates>
MODE           : <lite | full | plan>
```

---

## 4. Stop Rule — don't let the dialogue become the haystack

Advance out of the dialogue when **any** holds: (a) the Critical assumptions and the negative condition are pinned;
(b) further questions wouldn't change the design; (c) the user signals "enough"; (d) in lite mode, after one
clarifying pass; (e) diminishing returns — you are doubting for its own sake. Methodic doubt is **constructive**: it
terminates at a stable footing, not at the destruction of everything.

---

## 5. Modes

- **Plan / full** — run all stages (compress 0–1 if the request is already sharp).
- **Lite / chat** — one pass: restate + a single clarifying question (or stated `[assumed]` answers) + purpose + scope
  + negative condition, then proceed. **Never skip the negative condition** — even a chat answer must know what
  "not found" would look like.

---

## 6. Anti-patterns

Interrogation fatigue (too many questions) · leading questions (Socratic ≠ leading) · accepting the user's first
framing as the question · letting solution/topic/source words sneak into the Question Core · infinite doubt that
never reaches a footing · doubting cheap assumptions while ignoring the load-bearing ones.

---

## 7. References

Verified live via domain-scoped search retrieval on 2026-06-22; raw byte-level fetch was blocked environment-wide
during this research (see the verification note in `paradigm.md` §5). Shared philosophy refs (Dewey; abductive
analysis — Timmermans & Tavory, Charmaz) live in `paradigm.md` §5.

1. SEP, *Descartes' Method* (methodic / hyperbolic doubt as a constructive procedure) — https://plato.stanford.edu/entries/descartes-method/ ; IEP corroboration — https://iep.utm.edu/rene-descartes/
2. SEP, *Plato's Ethics* (Socratic *elenchus*: cross-examination from the interlocutor's own beliefs) — https://plato.stanford.edu/entries/plato-ethics-shorter/
3. FINER criteria for a good research question — https://pmc.ncbi.nlm.nih.gov/articles/PMC2912019/
4. PICO(T) format for answerable empirical/clinical questions — https://pmc.ncbi.nlm.nih.gov/articles/PMC3430448/

*Method acknowledgment:* the staged-doubt procedure is adapted from the `doubt` planning skill (Descartes, *Discourse
on Method*, 1637), retargeted from product planning to research framing.

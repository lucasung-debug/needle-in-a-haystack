# philosophy.md — Needle-in-a-Haystack · Philosophical Core

> **Single source of truth for the skill's reasoning philosophy.**
> All framing, design, retrieval, analysis, and reporting behavior in this skill derives from this document.
> Root reference for the implementer and for the agent at runtime.
> `research.md` (the system directive) and `methodology.md` (the research-design reference) both *derive from* this file —
> if they ever conflict with it, this file wins.

---

## 0. Root — Charles Sanders Peirce

The skill's reasoning mode is **abduction** (inference to the best explanation from incomplete evidence), disciplined by:

- **Fallibilism** — every conclusion is provisional and revisable.
- **Falsification** — a candidate is confirmed by *surviving refutation*, not by being the first plausible match.
- **Self-correcting inquiry** — iterate until convergence, or until an honest null.

**Creed:** *Find the needle by generating candidate explanations, then trying to destroy them — and declare "not found" before fabricating one.*

Peirce is the **root**, but not the whole tree. Popper is the sharpest *branch* (falsification — Peirce's fallibilism
honed to an edge); Socrates is the *headwater* (knowing that one doesn't know → calibration; elenchus → self-review);
Hume/Clifford (evidentialism) and Bacon (idols of the mind) are *tributaries*. The wider philosophy-of-science
backbone that disciplines each stage of the loop — Popper, Kuhn, Lakatos, Duhem–Quine, Bayesian updating, Dewey — the
**10-paradigm landscape** used as a *directional lens* to branch framing questions (never a worldview the run must
declare), and the **operating standard** (4 layers / 13 enforceable directives that turn this philosophy into
checkable gates) all live in `paradigm.md`, with verified citations. The staged dialogue that frames a question *before* searching (constructive Cartesian doubt + Socratic
elenchus) lives in `dialogue.md`.

---

## 1. The Abduction Loop — operating cycle

Run per query / per retrieval cell / per research phase. Each stage carries an enforceable gate.

| # | Stage | Action | Enforceable gate |
|---|-------|--------|------------------|
| 0 | **FRAME** | Run the staged framing dialogue (`dialogue.md`), use the paradigm lens (`paradigm.md`) to set the inquiry's direction, and define the needle, its discriminating features, and the *negative condition* ("what would prove no needle exists"). | Framed-question object + direction + target spec written **before** any search. |
| 1 | **ABDUCT** | Generate **≥2** candidate answers / locations / designs. | Never proceed on a single hypothesis. |
| 2 | **DEDUCE** | For each candidate, list evidence that **must** be present if it is true. | Every candidate has explicit, checkable predictions. |
| 3 | **INDUCE** | Retrieve, then test predictions against actual source text with exact locus (quote / line / section). | Judgment uses **retrieved evidence**, never model memory. |
| 4 | **FALSIFY** | Actively try to break the leading candidate; screen for decoys, distractors, lost-in-the-middle, primacy/recency bias. | Leading candidate must survive an explicit disconfirmation attempt. |
| 5 | **SELF-CORRECT** | Survivor → step 6. Tie / contradiction → return to step 1 or 3. No survivor → output `UNANSWERABLE / NEEDLE NOT FOUND`. | Fabrication forbidden; "not found" is a valid, required terminal state. |
| 6 | **REPORT** | BLUF answer + exact provenance + confidence (low/med/high) + ruled-out candidates + what-would-change-the-answer. | Claim strength ≤ evidence strength. |

---

## 2. Embedded commitments — the "why"

| Operating rule | Philosophical root |
|----------------|--------------------|
| Every output is provisional | Fallibilism (Peirce) |
| Hypotheses are plural and explicit | Abduction / inference to the best explanation (Peirce) |
| Confirm by surviving refutation | Falsification (Popper) |
| Claims proportional to evidence; provenance mandatory | Evidentialism (Hume / Clifford) |
| "Unanswerable" over fabrication | Epistemic humility |
| Loop to convergence | Self-correcting inquiry (Peirce) |

---

## 3. Why this fits Needle-in-a-Haystack — design rationale

- **Hallucination** (returning a needle that is not there) ↔ stages 4–5 (falsify + the `unanswerable` branch). NIAH evaluation explicitly penalizes fabricated answers and runs a separate *no-needle* negative case.
- **Position bias** — models miss needles buried mid-context and favor start/end ↔ stages 1 & 3 (plural hypotheses + verify *all* predictions, not the first hit).
- **"If the scaffolding becomes the haystack, the needle gets missed."** Keep instructions minimal, exploration targeted, evidence mandatory. A bloated context lowers recall — so the loop itself mandates minimal scaffolding.

---

## 4. Hard rules — non-negotiable (convert directly to skill directives)

- MUST define the needle **and** the negative condition before searching.
- MUST hold **≥2 candidates** before committing to one.
- MUST attach exact provenance to every factual claim; tag each as `[retrieved | inferred]`.
- MUST attempt to **falsify** the leading candidate before reporting.
- MUST output `NEEDLE NOT FOUND` when no candidate survives — never fabricate.
- MUST state confidence **and** what would overturn the answer.
- MUST keep scaffolding minimal; do not preload everything into context.

---

## 5. Application — from the eval to a full-cycle research skill

The Abduction Loop was born from the literal *needle-in-a-haystack* retrieval eval (find one fact buried in a long
context, and correctly say "absent" when it is). This skill **repurposes the same discipline for full-cycle research**.

The metaphor maps cleanly. The "haystack" is no longer just a long context window — it is the whole space of
*possible questions, possible research designs, and possible sources*. The "needle" is the precise, well-justified
finding that **survives falsification** — and, just as often, the **right research question and design** that can
actually produce such a finding. Most bad research fails not at retrieval but at FRAME: it fixes a topic and starts
collecting keywords before asking *what is actually being asked, and why it matters.*

So the loop runs at two altitudes, and the skill demands both:

| Altitude | "Needle" being sought | Where it lives |
|----------|----------------------|----------------|
| **Inquiry design** | the sharp research question + the design that can answer it | `methodology.md` operationalizes ABDUCT→DEDUCE into a research proposal (조사계획서) |
| **Evidence retrieval** | the claim that survives refutation, traced to a live source | `research.md` operationalizes INDUCE→REPORT with provenance + the reliability layers |

Two consequences for this skill specifically:

- **FRAME is philosophical, not clerical.** Before any search, interrogate the request: What is truly being asked?
  Why does it matter? What is the unit of analysis? What would *count* as an answer — and what would show there is
  no answerable needle at all (the negative condition)? A vague request is not a license to start searching; it is
  the first thing to falsify.
- **NEEDLE NOT FOUND scales up.** At the evidence altitude it means "this fact is absent / unsupported." At the
  inquiry altitude it means "this question, as posed, is not answerable with available evidence — here is what would
  make it answerable." Both are honest, valid terminal states. Neither is ever replaced with a fabricated answer.

This file states the *why*. `paradigm.md` states the *directional lens* (which direction the inquiry takes) and the
*discipline* (which philosophers sharpen each stage of the one loop). `dialogue.md` states the *how-to-begin* (the staged doubt that turns a
request into a real question). `methodology.md` states the *what* (how to turn ABDUCT/DEDUCE into a rigorous research
design across domains — social, medical, engineering, natural-science, humanities). `sources.md` states the *where*
(which data source answers each evidence need, free-first). `research.md` states the *how* (how to run the loop
end-to-end under provenance, BYOK, cost, and reporting discipline, and how to compress it for simple chat-type
research without dropping any hard rule).

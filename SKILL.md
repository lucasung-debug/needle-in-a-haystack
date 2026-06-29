---
name: needle-in-a-haystack
description: >
  Full-cycle research skill for any domain (social, engineering, medical, natural sciences, humanities),
  with abductive reasoning (Peirce) as its single root. Don't fix a topic on reflex — run a staged framing
  dialogue (constructive Cartesian doubt + Socratic questioning), use a paradigm lens to branch the inquiry's
  direction (regularity/meaning/mechanism/what-works/power), design a falsifiable research plan (조사계획서/protocol),
  route data sources under BYOK + free-first cost discipline (recommend useful research APIs the user could add),
  collect under PROVENANCE, try to break the finding, and report what survives. Scales from a formal study design
  down to simple chat-type research. Outputs "NEEDLE NOT FOUND" before fabricating an answer.
  Triggers — "research", "조사", "research plan/proposal", "조사계획서", "literature review", "study design",
  "find the needle", "is this true / verify this", "deep research", "byok research".
  Skip when — the user wants a quick non-research answer or creative writing; a more specific collector skill
  already owns the task (e.g. a dedicated web-search/news/video skill); or they explicitly opt out of sourcing.
triggers:
  - needle in a haystack
  - full-cycle research
  - research plan
  - 조사계획서
  - research design
  - research protocol
  - literature review
  - falsify don't confirm
  - byok research
  - research data api
  - provenance check
  - unanswerable over fabrication
  - clarify research question
  - research paradigm
  - research philosophy
  - analytic standards
  - methodic doubt
allowed-tools: [Read, Write, Bash, WebSearch, WebFetch, AskUserQuestion]
---

# needle-in-a-haystack — Full-Cycle Research Skill

Obey `references/research.md` before producing, planning, executing, merging, or validating any research output.

## Pipeline Context
| 항목 | 내용 |
|---|---|
| **Position** | Self-contained full-cycle research skill: FRAME → DESIGN → ROUTE & COST → COLLECT → FALSIFY → SELF-CORRECT → REPORT. |
| **Input** | A research request / question (one line to a full brief). |
| **Output** | A research plan (조사계획서) and/or a cited report, always closing with the compliance block. cwd-relative artifact paths. |
| **Companions** | Optional collector skills (web-search/news/video/social) if installed; this skill governs them under LAW 0. |
| **Handoff** | plan → execute may split sessions: write `.claude/handoffs/handoff-<ts>.json` (framed-question object + plan path + mode), resume by reading it. |

## MUST DO / MUST NOT DO (above the steps)
- ✅ Define the **needle AND the negative condition** before searching; set the inquiry **direction**.
- ✅ Hold **≥2 candidates**; **try to falsify** the leader before reporting.
- ✅ Attach **provenance** to every factual claim, tagged `[retrieved | inferred | assumed]` (LAW 0).
- ✅ Separate **confirmed** (retrieved + corroborated) from **unconfirmed/unknown**; write "cannot confirm" over a hedge ("probably / maybe / 아마").
- ✅ Ask via **`AskUserQuestion`** (templates/askuserquestion.snippet.json); map each option 1:1 to a real next action.
- ✅ Gate the output with the **script**, not by eye: `python ${CLAUDE_SKILL_DIR}/scripts/compliance_check.py <output.md>`.
- ⛔ Never fabricate a needle — output **`NEEDLE NOT FOUND`** when nothing survives.
- ⛔ Never tune a finding to the user's expectation (independence / anti-sycophancy).
- ⛔ Never let paradigms become co-equal foundations — **abduction is the single root**; they are a directional lens.
- ⛔ Never dump SKILL/report internals into chat — write to a file and summarize.

## Run
1. Load `references/research.md` (the system directive). It runs the full cycle and carries LAW 0, the 4 layers, BYOK/cost, modes, and the compliance block.
2. At the start of FRAME, run `references/dialogue.md` (staged framing dialogue) to turn the request into a real question; use the **paradigm lens** in `references/paradigm.md` to branch the inquiry's *direction* (not a worldview to declare). Ask with `templates/askuserquestion.snippet.json`.
3. The single reasoning root is `references/philosophy.md` (the Abduction Loop — Peirce); `references/paradigm.md` adds the directional lens + the philosophers who *discipline* (don't rival) that one loop. Load when FRAME/FALSIFY needs the *why*.
4. For a research-plan / study-design request, load `references/methodology.md` (domain-general design) during DESIGN; draft from `templates/proposal.template.md`.
5. During ROUTE & COST, consult `references/sources.md` to route each evidence need free-first and surface NICE-TO-HAVE API recommendations instead of silently dropping evidence.
6. At FALSIFY, run `references/falsify-skeptic.md` (author ≠ reviewer) to attack the leading candidate across seven named failure modes; fill `templates/skeptic-scorecard.snippet.md`. Mark `[FALSIFY]=PASS` **only** on a PASS scorecard — otherwise loop back (REWORK the named mode) or output **NEEDLE NOT FOUND**.
7. REPORT from `templates/report.template.md`, then **gate**: `python ${CLAUDE_SKILL_DIR}/scripts/compliance_check.py <output.md>` must exit 0. Add `--check-links` when online to *verify* `[L1] live` rather than assert it (offline → `unverified` is acceptable). If it exits non-zero, fix the output (do not ship). Mark outputs that skip framing, provenance, or falsification as INVALID and redo.

## 참조 자료 (라우팅 테이블)
If unsure which reference a phase needs, read `references/_index.md` first, then open **exactly one** file.

| Topic | Reference | Load When |
|---|---|---|
| system directive (정전) | references/research.md | always, first — runs the full cycle + compliance |
| the *why* (abduction root) | references/philosophy.md | FRAME/FALSIFY need the reasoning root |
| directional lens + discipline | references/paradigm.md | FRAME (set direction) · FALSIFY (apply the gates) |
| staged framing dialogue | references/dialogue.md | start of FRAME (plan/full); compressed in lite |
| research-design (조사계획서) | references/methodology.md | DESIGN, when producing a plan/protocol |
| data-source catalog + BYOK | references/sources.md | ROUTE & COST, mapping evidence → source |
| skeptic-judge (반증) | references/falsify-skeptic.md | FALSIFY — attack the leader across 7 failure modes, fill the scorecard |

## Templates & gates
- `templates/` — fill placeholders only: `proposal.template.md` (조사계획서), `report.template.md`, `report.html` (self-contained, zero-dep shareable view), `framed-question.template.md`, `compliance-block.snippet.md`, `skeptic-scorecard.snippet.md`, `askuserquestion.snippet.json`.
- `scripts/compliance_check.py` — the validator-as-gate for every output (exit non-zero = don't ship).
- `eval/runner.py` — frozen regression: `python ${CLAUDE_SKILL_DIR}/eval/runner.py` (exit 0 = detection==1.0 & FP==0). After editing `compliance_check.py`, rerun it; raise the bar by adding adversarial fixtures, never by editing the judge.

Keep scaffolding minimal — load depth only when the phase needs it. If the scaffolding becomes the haystack, the needle gets missed.

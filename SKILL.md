---
name: needle-in-a-haystack
description: Full-cycle research skill for any domain (social, engineering, medical, natural sciences, humanities). Don't fix a topic on reflex — philosophically frame WHAT must be investigated and WHY, design a falsifiable research plan (조사계획서/protocol), route data sources under BYOK + free-first cost discipline (and recommend useful research APIs the user could add), collect under PROVENANCE, try to break the finding, and report what survives. Scales from a formal study design down to simple chat-type research. Outputs "NEEDLE NOT FOUND" before fabricating an answer.
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
---

# needle-in-a-haystack — Full-Cycle Research Skill

Obey `research.md` before producing, planning, executing, merging, or validating any research output.

1. Load `research.md` (the system directive). It runs the full cycle: **FRAME → DESIGN → ROUTE & COST → COLLECT → FALSIFY → SELF-CORRECT → REPORT.**
2. The reasoning root is `philosophy.md` (the Abduction Loop — Peirce). Load it when FRAME or FALSIFY needs the *why*.
3. For a research-plan / study-design request, load `methodology.md` (domain-general design — social/medical/engineering/natural-science/humanities) during DESIGN.
4. During ROUTE & COST, consult `sources.md` (research-data source catalog) to route each evidence need free-first, and recommend useful APIs the user could add (NICE-TO-HAVE) instead of silently dropping evidence.
5. Enforce the hard rules at every size: define the needle **and** the negative condition first; hold **≥2 candidates**; attach provenance to every claim; **try to falsify** before reporting; output **`NEEDLE NOT FOUND`** rather than fabricate; state confidence + what would change the answer.
6. Close every output with the compliance block in `research.md`. Mark outputs that skip framing, provenance, or falsification as INVALID and redo them.

Keep scaffolding minimal — load depth (`philosophy.md`, `methodology.md`, `sources.md`) only when the phase needs it. If the scaffolding becomes the haystack, the needle gets missed.

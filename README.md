# needle-in-a-haystack — Full-Cycle Research Skill

A Claude skill (Claude Code CLI / app) that runs research as a **full cycle**, not a keyword search with a summary
glued on — across any domain (social science, engineering, medicine, natural sciences, humanities). BYOK (Bring
Your Own Key) — works with zero keys, gets richer as you add your own.

## What

Most research fails before retrieval, at the framing: it fixes a topic on reflex and starts collecting keywords
before asking *what is actually being investigated, and why.* This skill refuses that. It:

1. **FRAME via a staged dialogue** — instead of accepting the request at face value, it runs a *framing dialogue* (constructive Cartesian doubt + Socratic questioning, adapted from the `doubt` planning skill): surfaces hidden assumptions and strips the request to the real question (no premature topic/method). A **paradigm lens** branches the inquiry's *direction* — regularity/measurement, meaning, mechanism, what-works, or power/change — which quietly decides *what counts as evidence* (no formal paradigm declaration required). It also fixes the *negative condition* (what would show there's no answerable needle).
2. **DESIGN** — generates ≥2 candidate answers or research designs, and for a study request produces a rigorous, falsifiable **research plan** (조사계획서 / protocol). Domain-aware: it carries the design families, evidence hierarchies, and reporting standards for social science, medicine/clinical (PICO, GRADE, PRISMA), engineering/CS (reproducibility, benchmarks, prior art), natural sciences, and the humanities.
3. **ROUTE & COST** — maps each evidence need to the right data source free-first (most scholarly/clinical/patent/dataset APIs are free or keyless — OpenAlex, Crossref, arXiv, PubMed, ClinicalTrials.gov, World Bank…), estimates cost, and **recommends useful APIs you could add** ("이런 API 있으면 좋아요") instead of silently dropping evidence. Paid sources are gated by explicit consent.
4. **COLLECT** — retrieves under PROVENANCE, isolating fetched content as data, not instructions.
5. **FALSIFY** — tries to break the leading finding (decoys, position bias, single-source, confirmation bias).
6. **SELF-CORRECT** — loops on contradiction; outputs **`NEEDLE NOT FOUND`** rather than fabricate.
7. **REPORT** — BLUF + provenance + confidence + ruled-out candidates + what-would-change-the-answer.

The "needle in a haystack" is the precise, well-justified answer — or the right question and design — that survives
refutation. The same directive scales down to simple chat-type research without dropping a single hard rule.

## Why

A finding is not what you can assemble; it is what remains standing after you have tried to knock it down.
Falsification, plural hypotheses, and provenance are not features bolted onto research — they are its skeleton.
An output that skips framing, provenance, or falsification is invalid.

## Files

| File | Role |
|------|------|
| `SKILL.md` | Entry point — load `research.md` first. |
| `research.md` | The system directive (constitution): the 7-phase full cycle, LAW 0 provenance, the 4 reliability layers, BYOK + cost, modes, and the compliance block. |
| `philosophy.md` | The reasoning root — Peirce's Abduction Loop (FRAME→…→REPORT) and the epistemic commitments everything derives from. |
| `paradigm.md` | Subordinate to the abduction root — the **directional lens** (the 10-paradigm landscape used to *branch* the framing question's direction, not a worldview to declare); the **operating standard** (4 layers / 13 enforceable directives, grounded in intelligence-analysis tradecraft — Heuer ACH, ICD 203); and the philosophy-of-science backbone (Popper, Kuhn, Lakatos, Duhem–Quine, Bayes, Dewey) that *disciplines* the one loop. Carries 34 verified citations. Loaded during FRAME/FALSIFY. |
| `dialogue.md` | The staged framing dialogue — constructive Cartesian doubt + Socratic elenchus (adapted from the `doubt` skill) that turns a request into a real question before any search. Loaded at the start of FRAME. |
| `methodology.md` | Domain-general research-design reference (사회조사 + medical, engineering, natural-science, humanities) — turns a framed question into a falsifiable research plan; loaded on demand during DESIGN. |
| `sources.md` | Research-data source catalog + BYOK discovery — scholarly, clinical, patent, and dataset APIs (mostly free/keyless), with the NICE-TO-HAVE recommendation; loaded on demand during ROUTE & COST. |

## Install

1. Copy this folder to `~/.claude/skills/needle-in-a-haystack/`.
2. The skill auto-loads `research.md`; `philosophy.md` and `methodology.md` are loaded on demand (progressive disclosure — minimal scaffolding).
3. Copy `.env.example` to `.env` only if your runtime loads environment files; otherwise set the variables in your shell or secret manager.
4. Leave any missing key blank. Missing sources degrade to free fallback behavior.

## BYOK

No secrets are stored in this repository. All keys are optional and read from environment variables only.

| Env var | Unlocks | If absent |
|---|---|---|
| `(none)` | WebSearch and native agent tools | Always available |
| `OPENROUTER_API_KEY` | Perplexity-sonar or other cited verify/synthesize models | Native synthesis |
| `BRAVE_API_KEY` | Brave web search backend | Native WebSearch |
| `TAVILY_API_KEY` | Tavily web search backend | Native WebSearch |
| `EXA_API_KEY` | Exa web/code search backend | Native WebSearch |
| `XAI_API_KEY` | X/Twitter research via xAI/Grok-native route | WebSearch `site:x.com` |
| `YOUTUBE_API_KEY` | YouTube metadata and transcript discovery | WebSearch `site:youtube.com` |
| `NAVER_CLIENT_ID` | Naver Korean web/blog/cafe APIs | Korean WebSearch |
| `NAVER_CLIENT_SECRET` | Naver Korean web/blog/cafe APIs | Korean WebSearch |
| `SCRAPECREATORS_API_KEY` | TikTok, Instagram, Threads, Pinterest collectors | Skip those platforms |
| `GROQ_API_KEY` | Whisper transcription for caption-less video | Skip transcription |

Paid or metered providers require explicit per-run consent even when a key exists. Key presence is not spending permission.

**Research-data APIs** (scholarly, clinical, patents, datasets) are catalogued separately in `sources.md` — most are
free or keyless (OpenAlex, Crossref, arXiv, PubMed, ClinicalTrials.gov, OpenFDA, PatentsView, World Bank…). Optional
free keys (`SEMANTIC_SCHOLAR_API_KEY`, `NCBI_API_KEY`, `CORE_API_KEY`, `EPO_OPS_KEY`, …) only raise rate limits or
unlock extras; paid indexes (Scopus, Web of Science, IEEE, Cochrane) stay consent-gated. See `.env.example`.

## Output Contract

Every output ends with the compliance block defined in `research.md`. Every conclusion maps to a source URL, an
ISO-8601 UTC retrieval timestamp, and a live-link status — or it is labeled a hypothesis, not a finding.

## Grounding & provenance (the skill eats its own cooking)

The skill's reasoning is not asserted from memory — it was **built by running the skill's own discipline** (abduction
+ LAW 0 provenance) over the literature. `paradigm.md` and `dialogue.md` carry verified citations to primary sources:
the Stanford Encyclopedia of Philosophy (Peirce, Popper, Kuhn, Lakatos, Duhem–Quine, Bayesian epistemology, Dewey,
Descartes, Socratic elenchus, Hume/Clifford, Bacon, hermeneutics/phenomenology, social construction, new materialism),
official intelligence-analysis standards (CIA — Heuer's *Psychology of Intelligence Analysis* / ACH; ODNI ICD 203),
and peer-reviewed methodology literature (the 10 research paradigms; FINER/PICO; abductive analysis). Honest caveat,
recorded as the skill itself would require: during this research raw byte-level fetch was blocked environment-wide, so
sources were confirmed *live and content-matched via search retrieval*, not via a rendered fetch — re-verify in an
unrestricted network before treating as byte-level provenance.

## License

MIT. See `LICENSE`.

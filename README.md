# needle-in-a-haystack — Full-Cycle Research Skill

A Claude skill (Claude Code CLI / app) that runs research as a **full cycle**, not a keyword search with a summary
glued on. BYOK (Bring Your Own Key) — works with zero keys, gets richer as you add your own.

## What

Most research fails before retrieval, at the framing: it fixes a topic on reflex and starts collecting keywords
before asking *what is actually being investigated, and why.* This skill refuses that. It:

1. **FRAME** — philosophically interrogates the request (what is truly asked, why it matters, what would count as an answer, and the *negative condition* — what would show there's no answerable needle).
2. **DESIGN** — generates ≥2 candidate answers or research designs, and for a study request produces a rigorous, falsifiable **research proposal** (조사계획서) spanning question type, operationalization, sampling, validity/reliability, bias register, and ethics.
3. **ROUTE & COST** — maps each evidence need to a source/API under free-first discipline and estimates cost (paid sources gated by explicit consent).
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
| `methodology.md` | Social-research design reference (사회조사) — turns a framed question into a falsifiable research proposal; loaded on demand during DESIGN. |

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

## Output Contract

Every output ends with the compliance block defined in `research.md`. Every conclusion maps to a source URL, an
ISO-8601 UTC retrieval timestamp, and a live-link status — or it is labeled a hypothesis, not a finding.

## License

MIT. See `LICENSE`.

# research - Research Governance Skill

## What

`research` is a single Claude skill that acts as the governance gate for research-producing skills. It does not replace collectors such as `search-orchestration`, `storm-research`, `news-for-beginner`, `youtube-insight-miner`, `x-ai-trend`, or `last30days`; it defines the evidence contract they must obey.

This repository is named `needle-in-a-haystack`, but the skill it ships installs as `research` (the `name` in `SKILL.md`).

## Why

Research output is only useful when claims survive falsification and remain traceable to live sources. `research.md` enforces provenance, verification, prompt-injection isolation, graceful fallbacks, BYOK, and free-first cost discipline. An output that skips provenance or verification is invalid.

## Install

1. Copy this folder to `~/.claude/skills/research/`.
2. Ensure every research skill loads `~/.claude/skills/research/research.md` before emitting conclusions. Add a line like this to each research skill's `SKILL.md`:

   ```text
   Before emitting any research conclusion, load and obey
   `~/.claude/skills/research/research.md` (the research governance gate).
   ```

3. Copy `.env.example` to `.env` only if your runtime loads environment files; otherwise set the variables in your shell or secret manager.
4. Leave any missing key blank. Missing sources degrade to free fallback behavior.

## BYOK

No secrets are stored in this repository. All keys are optional and read from environment variables only.

The canonical BYOK table lives in `research.md`; the table below is a summary and must stay in sync with it.

| Env var | Unlocks | If absent |
|---|---|---|
| `(none)` | WebSearch and native agent tools | Always available |
| `OPENROUTER_API_KEY` | Perplexity-sonar or other cited verify/synthesize models | Native synthesis |
| `BRAVE_API_KEY` | Brave web search backend | Native WebSearch |
| `TAVILY_API_KEY` | Tavily web search backend | Native WebSearch |
| `EXA_API_KEY` | Exa web/code search backend | Native WebSearch |
| `XAI_API_KEY` | X/Twitter research via xAI/Grok-native route | WebSearch `site:x.com` |
| `YOUTUBE_API_KEY` (+ `yt-dlp` installed) | YouTube metadata and transcript discovery | WebSearch `site:youtube.com` |
| `NAVER_CLIENT_ID` / `NAVER_CLIENT_SECRET` | Naver Korean web/blog/cafe APIs | Korean WebSearch |
| `SCRAPECREATORS_API_KEY` | TikTok, Instagram, Threads, Pinterest collectors | Skip those platforms |
| `GROQ_API_KEY` | Whisper transcription for caption-less video | Skip transcription |

Paid or metered providers require explicit per-run consent even when a key exists. Key presence is not spending permission.

## Output Contract

Every governed research output must end with the compliance block defined in `research.md`. Every conclusion must map to a source URL, ISO-8601 UTC retrieval timestamp, and live-link status.

Check a block mechanically with the bundled validator (Python 3 standard library only):

```sh
python3 scripts/validate_compliance.py output.txt   # or pipe via stdin
```

Exit code 0 means the block is present, well-formed, and internally consistent (no `FAIL` gate under a `VALID` final verdict, no paid use without recorded consent). Sample outputs live in `scripts/fixtures/`.

## License

MIT. See `LICENSE`.

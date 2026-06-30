# sources.md — Research-Data Source Catalog & BYOK Discovery

> Derived from `research.md`. Loaded on demand during **ROUTE & COST (Phase 2)**.
> Purpose: map each evidence need from DEDUCE to the *right* authoritative data source, prefer free/keyless sources,
> and — when the best-fit source needs a key the user lacks — surface a **NICE-TO-HAVE** recommendation ("이런 API
> 있으면 좋아요") stating what it unlocks, its tier, and the env var, instead of silently skipping the evidence.
> Most high-value research APIs (scholarly, clinical, patents, datasets) are **free or keyless** — this fits the
> free-first rule, so a zero-key user already reaches most of the literature.

---

## 0. Tier legend & routing rule

| Tier | Meaning | Routing priority |
|------|---------|------------------|
| `keyless` | works with no key (a polite-pool email is courteous, never required) | **try first** |
| `free-key` | free API key only raises rate limits / unlocks extras | second |
| `paid` | subscription or metered; consent-gated by the `research.md` interlock | last, only on explicit consent |

**Rule (ROUTE phase):** for each evidence need, pick the narrowest authoritative source, `keyless` → `free-key` →
`paid`. Never invent an endpoint or a result. If a source is `paid`, or `free-key` and the user has no key, do not
silently drop the need — proceed with the free fallback **and** emit the NICE-TO-HAVE block in §11.

> **This catalog is a curated starter set, not a closed list.** If the best-fit source for an evidence need isn't
> here (a niche domain — legal/case-law, financial filings, geospatial/earth-observation, news archives…), recommend
> it the *same way*: name it, its tier, the env var (§11) — then BYOK and **use it**. Grow the recommendation to fit
> the question; never cap the research at the rows below.

> No secrets live here. All keys are read from environment variables only (BYOK); every row degrades to a fallback.

### Source recipe (when a source is tricky to crack)

When a source needs a non-obvious move to work (an auth header, a sitemap-vs-API choice, a rate quirk), record a short
recipe so the next run doesn't rediscover it — **boundary · why the generic path fails · the working path · the
fallback · the pitfall**. Worked example (SEC EDGAR):

> **boundary** data.sec.gov / efts.sec.gov · **generic fails** a plain GET returns 403 · **working** send a
> `User-Agent: Name email` header (no key needed), ≤10 req/s · **fallback** the filing's index page on www.sec.gov ·
> **pitfall** a missing User-Agent is the #1 cause of 403s.

---

## 1. Scholarly literature (all domains)

| Source | Unlocks | Tier | Env / note | Free fallback |
|--------|---------|------|-----------|----------------|
| **OpenAlex** | ~250M works, authors, venues, citations, concepts | `keyless` | `OPENALEX_MAILTO` (polite pool) | — (already free) |
| **Crossref** | DOI metadata, references, funders | `keyless` | `CROSSREF_MAILTO` (polite pool) | — |
| **Semantic Scholar** | paper graph, TLDRs, citation contexts, embeddings | `free-key` | `SEMANTIC_SCHOLAR_API_KEY` (raises rate limit) | keyless lower-rate access |
| **Unpaywall** | legal open-access full-text location for a DOI | `keyless` | `UNPAYWALL_EMAIL` (required param) | search the title on the web |
| **CORE** | aggregated OA full texts | `free-key` | `CORE_API_KEY` | OpenAlex / Unpaywall |
| **DOAJ** | open-access journal & article metadata | `keyless` | — | OpenAlex |
| **Scopus / Elsevier** | citation/abstract index (institutional) | `paid` | `SCOPUS_API_KEY` | OpenAlex + Crossref |
| **Web of Science** | curated citation index | `paid` | `WOS_API_KEY` | OpenAlex |

---

## 2. Medicine / clinical / life sciences

Pair these with the clinical evidence hierarchy in `methodology.md` §2 (PICO, GRADE, PRISMA, risk of bias).

| Source | Unlocks | Tier | Env / note | Free fallback |
|--------|---------|------|-----------|----------------|
| **PubMed / NCBI E-utilities** | biomedical literature (MEDLINE) | `keyless` | `NCBI_API_KEY` (3→10 req/s) | keyless lower-rate |
| **Europe PMC** | life-science literature + full text + preprints | `keyless` | — | PubMed |
| **ClinicalTrials.gov** | registered trials, status, outcomes | `keyless` | — | web search |
| **OpenFDA** | drug/device/food adverse events, labels, recalls | `keyless` | `OPENFDA_API_KEY` (raises limit) | keyless lower-rate |
| **Cochrane Library** | systematic reviews | `paid` | `COCHRANE_API_KEY` | PubMed `systematic[sb]` filter |

---

## 3. Engineering / CS / patents / standards

| Source | Unlocks | Tier | Env / note | Free fallback |
|--------|---------|------|-----------|----------------|
| **arXiv** | preprints (CS, EE, physics, math, stat) | `keyless` | — | OpenAlex |
| **Semantic Scholar** | CS/eng paper graph + code links | `free-key` | `SEMANTIC_SCHOLAR_API_KEY` | keyless |
| **PatentsView (USPTO)** | US patent data & prior art | `keyless` | — | web search |
| **EPO Open Patent Services** | European/worldwide patents | `free-key` | `EPO_OPS_KEY` / `EPO_OPS_SECRET` | PatentsView (US only) |
| **Lens.org** | scholarly + patent linkage | `free-key` | `LENS_API_TOKEN` | OpenAlex + PatentsView |
| **IEEE Xplore** | IEEE papers & standards | `paid` | `IEEE_API_KEY` | arXiv + Semantic Scholar |

> Standards bodies (ISO/IEC/IETF/W3C/NIST): cite the official spec page directly; most are web-fetchable.

---

## 4. Datasets & official statistics

| Source | Unlocks | Tier | Env / note | Free fallback |
|--------|---------|------|-----------|----------------|
| **World Bank** | development indicators by country/year | `keyless` | — | — |
| **OECD / Eurostat** | OECD & EU official statistics | `keyless` | — | — |
| **data.gov** & national open-data portals | government datasets | `keyless` | — | — |
| **Our World in Data** | curated long-run global metrics | `keyless` | — | — |
| **US EIA** | US & international energy statistics (production, prices, consumption) | `free-key` | `EIA_API_KEY` (free, instant) | data.gov / Our World in Data |
| **Zenodo / figshare / OSF / Dryad** | research datasets & materials (DOIs) | `keyless` | optional token for upload only | — |

---

## 5. Preprints

| Source | Unlocks | Tier | Env / note |
|--------|---------|------|-----------|
| **arXiv** | physics, CS, math, stat, econ, bio | `keyless` | — |
| **bioRxiv / medRxiv** | biology & medical preprints | `keyless` | — |
| **OSF Preprints / SSRN** | social science & multidisciplinary preprints | `keyless` | — |

> Preprints are not peer-reviewed — tag findings from them `[retrieved · preprint]` and weight accordingly in FALSIFY.

---

## 6. Web / general / social (carried from `research.md` BYOK)

WebSearch (keyless default) · Brave / Tavily / Exa (`free-key`/`paid`) · Perplexity-sonar via OpenRouter (`paid`, VERIFY/SYNTHESIZE) ·
Naver (`free-key`, Korean) · xAI/Grok, ScrapeCreators, YouTube, Groq-Whisper (see `research.md` BYOK table).

---

## 7. Law, legislation & regulation

A statute or ruling is a **primary source** — cite the official text, never a summary of it. Pair with the analytic-standards discipline in `paradigm.md`.

| Source | Unlocks | Tier | Env / note | Free fallback |
|--------|---------|------|-----------|----------------|
| **CourtListener (Free Law Project)** | US case law, opinions, oral arguments, PACER dockets (RECAP) | `free-key` | `COURTLISTENER_API_TOKEN` (token from your profile; many endpoints open by default) | the court's official opinion page |
| **Federal Register** | US federal rules, proposed rules, notices, executive orders | `keyless` | — | — |
| **GovInfo (US GPO)** | bills, public laws, US Code, CFR, Congressional record | `free-key` | `GOVINFO_API_KEY` (a free api.data.gov key) | Federal Register + official PDFs |

> EU law (EUR-Lex), UK legislation (legislation.gov.uk), and most national gazettes publish official, web-fetchable pages — cite those directly when no clean API exists.

---

## 8. Finance, company filings & economics

| Source | Unlocks | Tier | Env / note | Free fallback |
|--------|---------|------|-----------|----------------|
| **SEC EDGAR** | US public-company filings (10-K/10-Q/8-K), full-text search, company facts | `keyless` | `SEC_EDGAR_USER_AGENT` — SEC policy requires a `Name email` User-Agent (the polite-pool analogue); no key | — |
| **FRED (St. Louis Fed)** | US & international economic / financial time series | `free-key` | `FRED_API_KEY` (free, instant) | World Bank / OECD (§4) |
| **GLEIF (LEI)** | Legal Entity Identifiers — who an entity legally is + parent/child corporate structure | `keyless` | — (no registration) | OpenCorporates / official registry |

> Market/company data beyond filings (live prices, fundamentals) is mostly `paid` — route there only on the §11 consent interlock. Official statistics live in §4.

---

## 9. Geospatial, earth observation & climate

| Source | Unlocks | Tier | Env / note | Free fallback |
|--------|---------|------|-----------|----------------|
| **USGS Earthquake (FDSN event)** | global seismic event catalog (GeoJSON / QuakeML) | `keyless` | — | — |
| **NASA Open APIs** | earth imagery, EONET natural-event feed, planetary data | `free-key` | `NASA_API_KEY` (`DEMO_KEY` works for trials at a lower rate) | `DEMO_KEY` (rate-limited) |
| **Copernicus Data Space (Sentinel)** | EU Sentinel satellite imagery & products (STAC / OData / Sentinel Hub) | `free-key` | `CDSE_CLIENT_ID` / `CDSE_CLIENT_SECRET` (free OAuth registration) | NASA imagery |
| **Open-Meteo** | weather forecast + historical reanalysis (ERA5, from 1940), climate | `keyless` | — (non-commercial; ~10k calls/day) | NOAA CDO |
| **NOAA NCEI Climate Data Online** | US/global historical weather & climate station records | `free-key` | `NOAA_CDO_TOKEN` (free email signup; 10k/day, 5 req/s) | Open-Meteo (reanalysis) |

> US weather (`api.weather.gov`) and base maps (OpenStreetMap / Overpass / Nominatim) are keyless — fetch directly, no key.

---

## 10. News & media archives

| Source | Unlocks | Tier | Env / note | Free fallback |
|--------|---------|------|-----------|----------------|
| **GDELT DOC 2.0** | global news across 65 languages, rolling ~3-month full-text + tone/themes | `keyless` | — | WebSearch |
| **The Guardian Open Platform** | Guardian/Observer articles since 1999, full body text + tags | `free-key` | `GUARDIAN_API_KEY` (free developer key) | WebSearch |
| **Chronicling America (loc.gov API)** | historic US newspaper pages (12M+); served via the loc.gov JSON API since 2025 | `keyless` | — | — |

> News is reporting, not ground truth — corroborate a claim across ≥2 outlets in FALSIFY and prefer the primary document the article cites.

---

## 11. The NICE-TO-HAVE output (emit during ROUTE when a key is missing)

When the best-fit source for an evidence need is `paid`, or `free-key` and unset, append this to the routing plan —
never silently drop the evidence:

```text
[NICE-TO-HAVE] <evidence need>
  best-fit source : <name>  (<tier>)
  unlocks         : <what it would add vs the fallback>
  to enable       : set <ENV_VAR>  (free signup | paid)
  proceeding with : <free fallback used now>
```

Keep it to the sources that would actually change the result — do not list the whole catalog. This is the skill's
"이런 API 있으면 좋아요" surface: it tells the user exactly which key would have strengthened *this* finding, and
respects the cost interlock by never spending without consent.

---

## 12. .env

All env vars above are optional and listed in `.env.example`. Absent key → free fallback. Paid tiers (`SCOPUS_API_KEY`,
`WOS_API_KEY`, `IEEE_API_KEY`, `COCHRANE_API_KEY`, Perplexity-sonar) require the explicit per-run consent recorded in
the `[COST]` line of the compliance block.

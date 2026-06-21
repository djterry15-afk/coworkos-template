# CONTEXT.md
*Project: market-thesis — the live synthesis (L1-as-synthesis at the project tier).*

> **STOP:** read this project's `CLAUDE.md` before this file.

---

## CURRENT STATE

*(Placeholder — this is where your real thesis synthesis lives.)* What the question is, what's settled, the
open forks, and the current verdict (dated, additive). Probabilities/weighting are the human's call and land
here, never in the pipeline.

## THE WORKFLOWS BENEATH THIS PROJECT

Three helpers, one per role — this is the composed loop the template demonstrates:

- **`research-factory/`** *acquires* — one seed (a question) → discovers + grades external sources at the
  `01_source` gate → a source-grounded **brief** that stops short of a verdict. *(Sample run:
  `research-factory/_archive/sample-stress-metrics-lead-lag/` — "which stress metrics lead vs. lag?")*
- **`llm-wiki/`** *organizes* — an accepted brief's sources are ingested into pre-digested, linked pages,
  so the knowledge is cheap to consult later. *(See `llm-wiki/index.md`.)*
- **`stress-monitor/`** *monitors* — watches the metrics the research identified (funding-plumbing leads;
  credit spreads confirm, and lag) and renders a dated dashboard.
- **You** *conclude* — reason over brief + wiki + dashboard and update this `CONTEXT.md`.

**The seam:** research finds *which* metrics lead → the wiki files *why* → the monitor reports *where they
are now* → you decide. The two factories never load this synthesis at run time; each is self-contained.

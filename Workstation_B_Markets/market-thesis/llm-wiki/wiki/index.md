# llm-wiki — index (the control point)
*ILLUSTRATIVE. A pre-digested, LLM-maintained knowledge store for the parent **market-thesis** project. It
**organizes** sourced knowledge so it can be consulted cheaply; it does **not** acquire new evidence (that
is the `../../research-factory/`) and it does **not** conclude (that is the operator, in the project
`CONTEXT.md`). This is the **organize** role of acquire → organize → conclude.*

---

## What this is

The Karpathy "LLM wiki" pattern, scoped to one project: sources are **pre-digested on ingest** into linked
markdown pages, so a later question is answered by *reading the wiki*, not by re-reading raw sources (no
RAG at query time). Pages are short, cross-linked, and each claim traces to a graded source.

Three operations, defined in this wiki's [`../CLAUDE.md`](../CLAUDE.md) schema: **Ingest** a new source → a
page · **Query** the wiki → an answer written back into a page · **Lint** for contradictions/staleness.

## How it relates to its siblings

- **`../../research-factory/`** *acquires* — runs a seed → external evidence → a graded **brief**. When a brief
  is accepted, its sources are *ingested here* (a separate, downstream act — the factory never writes the
  wiki mid-run).
- **`../../stress-monitor/`** *monitors* — watches the metrics this knowledge identified as the ones that
  matter. The wiki explains *why* those metrics; the monitor reports *where they are now*.
- **`../../CONTEXT.md`** *concludes* — the operator reasons over the wiki + briefs + dashboard and records the
  verdict there.

## Pages

| Page | Covers |
|---|---|
| [financial-stress-indicators](financial-stress-indicators.md) | which market metrics lead a stress event vs. which lag — the lead/lag structure behind the monitor's metric groups |

*Add a page per topic as sources are ingested. Keep pages short; link liberally. See `log.md` for the
ingest history.*

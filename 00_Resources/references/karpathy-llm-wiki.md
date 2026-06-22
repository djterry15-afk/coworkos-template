# Karpathy's LLM Wiki pattern (distillation)
*What this is: a digest, in our own words, of the pattern behind the `llm-wiki` used in this workspace. When
to use it: read it before setting up or reasoning about any wiki here.*
*Source: Andrej Karpathy, "LLM Wiki," public GitHub Gist
(gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — an intentionally abstract idea file. This is a
summary, not the original.*

---

## The core idea
RAG re-derives knowledge from scratch on every query — the model finds and reassembles fragments each time;
nothing accumulates. The LLM Wiki inverts this: the LLM **pre-digests sources on ingest** into a persistent,
interlinked markdown wiki that sits between you and the raw sources. Cross-references are built once,
contradictions flagged once, the synthesis kept current. The wiki is a **compounding artifact** — richer with
every source and every question. You source and ask; the LLM does the summarizing, filing, and
cross-referencing.

## The three operations (the whole interface)
- **Ingest** — read a source, extract, update entity/concept pages, update the index, append the log. One
  source can touch many pages.
- **Query** — read the index, drill into the relevant pages, answer with citations. **File good answers back
  as pages** so explorations compound just like ingested sources — the non-obvious, load-bearing move.
- **Lint** — periodic health check: contradictions, stale claims, orphan pages, missing concept pages.

## What it leaves to the implementor
Directory structure, page format, tooling, and search infrastructure are all deferred — "at small scale the
index file is enough" (no embeddings required). The only non-negotiables: the **three operations** and a
**schema document** (a `CLAUDE.md` that makes the LLM a disciplined maintainer rather than a generic chatbot).

## The lineage
The pattern closes on Vannevar Bush's 1945 **Memex** — a private, curated knowledge store with associative
trails between documents. Bush's unsolved problem was *who does the maintenance*: the cross-reference upkeep
and summary-freshness that make wikis decay. The LLM is the answer — it doesn't get bored and can touch a
dozen files in one pass.

## How this template uses it
The `llm-wiki/` under the market-thesis project is this pattern scoped to one project: `CLAUDE.md` is the
schema, `raw/` holds immutable sources, `wiki/` holds the digested pages plus `index.md` and `log.md`. It
*organizes* sourced knowledge — distinct from the research factory that *acquires* it and the operator who
*concludes*.

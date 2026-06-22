# LLM Wiki — schema & operating contract
*(Example.) The wiki's defining file — its **schema**. A pre-digested, LLM-maintained knowledge base for the
parent **market-thesis** project, in the Karpathy "LLM wiki" pattern: sources are digested **on ingest** into
linked markdown pages, so a later question is answered by reading the wiki, not by re-reading raw sources (no
RAG at query time). This `CLAUDE.md` **is** the schema — read it before working in the wiki.*

---

## Boundary — what this wiki is and isn't

- **Organizes, doesn't conclude.** Pages record *what sources say*; the synthesized thesis verdict lives in
  the project `CONTEXT.md` one level up — never duplicate it here.
- **Organizes, doesn't acquire.** New external evidence is found by the sibling `../research-factory/`
  (tier-4). Ingesting a factory run's snapshots into this wiki is a **separate, downstream act** done here.
- The three roles stay separate: factory *acquires* → wiki *organizes* → operator *concludes*.

## Folder structure

```
llm-wiki/
├── CLAUDE.md       ← this file — the schema
├── raw/            ← source documents, immutable — never modify these
└── wiki/
    ├── index.md    ← table of contents (the control point — start here)
    ├── log.md      ← append-only record of every ingest / operation
    └── <topic>.md  ← the pages, flat, lowercase-with-hyphens
```

## Three operations

- **Ingest** a new source → read it fully, *discuss takeaways before writing*, create a source-summary page
  in `wiki/`, create/update concept pages, cross-link with `[[wiki-links]]`, update `wiki/index.md`, append
  to `wiki/log.md`. (One source may touch several pages — normal.)
- **Query** the wiki → read `wiki/index.md`, read the relevant pages, synthesize, cite the pages. If the
  answer isn't in the wiki, say so. A *valuable* answer is filed back into a page so it compounds.
- **Lint** → check for contradictions, orphan pages, missing concept pages, stale claims, format drift.

## Page format

Every page opens with **Summary** (1–2 sentences), **Sources** (the `raw/` files it draws from), and
**Last updated** (date). Source-summary pages add **Author / Published / URL** when known (lint uses
*Published* to flag stale claims). Then short, cross-linked prose.

## Citation rules

- Every factual claim references its source — `(source: filename)` after the claim.
- If two sources disagree, note the contradiction explicitly.
- A claim with no source is marked as needing verification — never faked.

## Ingesting from a research-factory run

When sources arrive from a `../research-factory/` run (not a manual drop in `raw/`): copy the run's
provenance-stamped snapshots into `raw/`, write the source-summary pages, and record the run name in the
page's prose as the "how found" (e.g. *acquired via research-factory run `<slug>`*) — **not** as a
wiki-linked source page. The factory is a workflow, not a source.

## Rules

- Never modify `raw/`. Always update `wiki/index.md` and `wiki/log.md` after changes. Page names
  lowercase-with-hyphens. Plain language. When unsure how to categorize, ask.

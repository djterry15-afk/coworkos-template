# Markdown vs. Database for AI Memory — cross-member study
*Date: 2026-06-22 | reference-study container | (EXAMPLE distillation — illustrative.)*

---

## The question
Across the three members, what decides whether an AI knowledge base should be **plain markdown** or a
**database** (graph / vector)?

## What the members said
- **markdown-wiki-pattern** (Karpathy LLM Wiki) — markdown + an index is enough at personal scale; the work
  is done at ingest (pre-digest), so query is a cheap read.
- **obsidian-pkm-guide** — confirms it in practice: a real PKM runs on `CLAUDE.md` + `index.md`, ~80% of the
  value with no infrastructure.
- **vector-memory-platform** (cognee) — a database-first system that genuinely works — but built for
  multi-agent / multi-tenant / hosted scale.

## The cross-member conclusion
Not "markdown beats databases." The members **agree once you add scale as the axis**: *personal-scale
knowledge tools converge on markdown-first; platform-scale products converge on databases.* The counterexample
sharpens the boundary instead of breaking it — and all three share the deeper move (**pre-digest on ingest**),
differing only in substrate (markdown vs. graph).

## Why it's logged here, not in a member's CONTEXT
This conclusion spans the members — no single one holds it. It compiles up into the container `CONTEXT.md`;
this file is the trace-to-source behind that synthesis line.

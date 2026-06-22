# CONTEXT.md
*Project: reference-study — the container's cross-member synthesis (Reasoning Workspace).*
*This IS a synthesis — unlike a flat Reference Repo's `CONTEXT.md`, which is thin or absent. It compiles what
has been learned ACROSS the members.*

> **STOP:** read this project's `CLAUDE.md` before this file.

---

## STUDIED — members with findings

- **markdown-wiki-pattern** — pre-digest-on-ingest; markdown + index suffices at personal scale. →
  `markdown-wiki-pattern/CONTEXT.md`
- **obsidian-pkm-guide** — worked markdown-first PKM; ~80% of the value without infrastructure. →
  `obsidian-pkm-guide/CONTEXT.md`
- **vector-memory-platform** — database-first (graph + vector) at multi-tenant / hosted scale. →
  `vector-memory-platform/CONTEXT.md`

## CROSS-MEMBER SYNTHESIS

*(EXAMPLE — the point of the container.)* **`markdown-wiki-pattern` and `obsidian-pkm-guide` converge:** at
personal scale, a plain-markdown knowledge base with a `CLAUDE.md` schema + an `index.md` control point is
sufficient — no vector DB required; the work is done at *ingest*, not at *query*. **`vector-memory-platform`
is the counterexample** — a successful database-first system — but its design center is multi-agent /
multi-tenant / hosted scale. It does **not** break the rule; it **sharpens the boundary**: *personal-scale
knowledge tools converge on markdown-first; platform-scale products converge on databases.* That boundary is
the conclusion **no single member states on its own** — it exists only across the three, which is exactly why
this container is a Reasoning Workspace and not a flat Reference Repo.

## CONNECTIONS

*(EXAMPLE.)* The markdown-first conclusion is the design rationale behind this template's own file-based,
no-database structure — the study backs the build. A cross-member conclusion that bore on another domain
would also earn a row in `00_Resources/cross-domain-map.md`.

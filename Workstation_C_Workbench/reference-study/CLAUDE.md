# CLAUDE.md — reference-study
*Project: reference-study — Workbench workstation. Kind · State: **Reasoning Workspace (study container) · Active.***
*Read ROOT CLAUDE.md → Workbench CLAUDE.md before reading this.*

---

## WHAT THIS PROJECT IS

*(Example — the "reason **across** references" pattern.)* A set of reference **sub-projects** — cloned repos,
papers, systems you study — that you **synthesize across** to extract patterns. Each member is a consult-from
reference in miniature; the **container** reasons across them toward conclusions the members can't hold on
their own.

That relationship is the whole point: **synthesize-across, not just consult → this container is a Reasoning
Workspace, not a Reference Repo** — even though every member, individually, is reference material. (Classify on
the *relationship* to the content, not its appearance.)

**Contrast its sibling `../reference-library/`:** that is a **flat Reference Repo** — entries you *pull* one at
a time, never reasoned across. Same domain, opposite relationship. Set side by side on purpose: the left case
(consult) and the right case (synthesize-across). This container mirrors the live `Reference_Repos` pattern.

## HOW IT'S ORGANIZED

- **Each member = its own folder** with its own `CLAUDE.md` (why it's here + what to extract) and `CONTEXT.md`
  (the findings from studying it — written *after* study, not on add). A member is a reference sub-project: you
  consult it.
- **The cross-member synthesis lives in this container's `CONTEXT.md`** — the patterns that emerge *across*
  members (convergences, contrasts, conclusions). This synthesis IS the reasoning the container does, and it
  is why this `CONTEXT.md` is a real synthesis (unlike a flat Reference Repo's, which has none).
- **`_reasoning-log/`** — dated cross-member study sessions (the container's reasoning trace), read by its
  `index.md`. *(The live system keeps this under the name `Notes/`; the template standardizes on
  `_reasoning-log/`.)*

## MEMBERS

*(EXAMPLE members — three reference sub-projects studied for the synthesis in `CONTEXT.md`. Each is
**referenced, not vendored** — the folder holds why it's here + findings, not the third party's files.
Replace with your own.)*
- **`markdown-wiki-pattern/`** — Karpathy's LLM Wiki (markdown-first, pre-digest-on-ingest).
- **`obsidian-pkm-guide/`** — Obsidian + Claude Code PKM (markdown-first, worked implementation).
- **`vector-memory-platform/`** — cognee (database-first; the counterexample).

## ROUTING

| Task | Go to | Load |
|---|---|---|
| Study one member deeply | that member's folder | its `CLAUDE.md` + `CONTEXT.md` |
| Synthesize across members / record a cross-cutting pattern | this container | this `CLAUDE.md` + `CONTEXT.md` (+ `_reasoning-log/`) |
| Add a new member | this container | create `<member>/` with its `CLAUDE.md` + `CONTEXT.md` |

## LOAD ORDER

ROOT CLAUDE.md (auto) → ROOT CONTEXT.md → Workbench CLAUDE.md → Workbench CONTEXT.md → this file →
this project's CONTEXT.md → (to study one) the member's `CLAUDE.md` + `CONTEXT.md`.

# CLAUDE.md Snippets
*What this is: copy-paste building blocks for the `CLAUDE.md` / `CONTEXT.md` files at any tier. When to use it:
when scaffolding a new tier or project — pull the block, fill the slots, delete the rest. When to skip: not
needed mid-reasoning — this is a create-time reference.*
*(ILLUSTRATIVE example entry — replace with your own reference material.)*

---

## Kind·state tag — project `CLAUDE.md`, first lines
> `*Project: <name> — <workstation> workstation. Kind · State: **<Reasoning Workspace | Reference Repo | Build/Workflow> · <Forming | Active | Dormant | Dead>.***`

The tag is the routing anchor — it changes rarely and tells the agent how to treat the project.

## STOP header — `CONTEXT.md`, top
> `> **STOP:** read this project's CLAUDE.md before this file.`

Enforces load order: `CONTEXT.md` is synthesis and doesn't make sense without the map above it.

## Routing-table skeleton — any `CLAUDE.md`
> ```
> | Task | Navigate to | Load | Skip |
> |---|---|---|---|
> | <task> | <child> | <files> | <the rest> |
> ```

The **Skip** column matters more than Load — it is what keeps context lean.

## Load-order block — project `CLAUDE.md`, bottom
> `ROOT CLAUDE.md (auto) → ROOT CONTEXT.md → <workstation> CLAUDE.md → <workstation> CONTEXT.md → this file → this project's CONTEXT.md → begin work.`

State the full chain so a cold session loads top-down before acting.

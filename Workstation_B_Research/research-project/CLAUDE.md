# CLAUDE.md
*Project: research-project — Research workstation. Kind · State: **Reasoning · Active.***
*Read ROOT CLAUDE.md → Research CLAUDE.md before reading this.*

---

## WHAT THIS PROJECT IS

*(Example.)* A standing research question or thesis you are building a grounded view of. This project
*concludes* — the verdict lands in `CONTEXT.md`. Two helpers sit beneath it: a wiki that *organizes* sourced
knowledge, and a tier-4 factory that *acquires* new external evidence. Acquire → organize → conclude are
distinct roles; keep them separate.

## WHERE THINGS LIVE

- **`CONTEXT.md`** — the live synthesis: the thesis state, what's settled, the open forks. Read it for state.
- **`research-factory/`** — the tier-4 workflow (exploratory fan-in). Acquires external evidence into a
  brief; self-contained, does **not** load this project's synthesis at run time.
- **`llm-wiki/`** — *(optional, not included in this example)* a standing store that organizes sources you
  consult repeatedly. The factory may *read* it and later *feed* it sources, but never writes it mid-run.
- **`references/`** — *reserved* — created only when a settled rule earns separation from state.

## LOAD ORDER

ROOT CLAUDE.md (auto) → ROOT CONTEXT.md → Research CLAUDE.md → Research CONTEXT.md → this file →
this project's CONTEXT.md. For a production run, instead enter at `research-factory/CLAUDE.md`.

# CLAUDE.md
*Project: market-thesis — Markets workstation. Kind · State: **Reasoning · Active.***
*Read ROOT CLAUDE.md → Markets CLAUDE.md before reading this.*

---

## WHAT THIS PROJECT IS

*(Example.)* A standing markets thesis you are building a grounded view of. This project *concludes* — the
verdict lands in `CONTEXT.md`. Three helpers sit beneath it, one per role:

- **`research-factory/`** *acquires* new external evidence (tier-4, exploratory fan-in) → a graded brief.
- **`llm-wiki/`** *organizes* the sourced knowledge so it is cheap to consult (a Layer-3 store).
- **`stress-monitor/`** *monitors* the metrics the research identified (tier-4, deterministic) → a dated dashboard.

**Acquire → organize → monitor → conclude** are distinct roles; keep them separate. The two tier-4 factories
are self-contained and do **not** load this project's synthesis at run time.

## WHERE THINGS LIVE

- **`CONTEXT.md`** — the live synthesis: the thesis state, what's settled, the open forks, the verdict.
- **`research-factory/`** — tier-4 (exploratory fan-in). Acquires external evidence into a brief.
- **`stress-monitor/`** — tier-4 (deterministic monitor). Fetches → transforms → renders a dated report.
- **`llm-wiki/`** — the organized source store: `CLAUDE.md` (the schema) · `raw/` (immutable sources) ·
  `wiki/` (`index.md` control point · `log.md` ingest log · topic pages). The factory may *read* it and,
  downstream, *feed* it; it is never written mid-run.
- **`references/`** — extracted **settled rules** (Layer 3), loaded by trigger. Holds `verdict-change-rule.md`
  — the standing rule for how the verdict is allowed to change. A rule lives here only once it has stopped
  moving; unsettled exploration stays in `CONTEXT.md` (an empty `references/` would be the over-engineering
  trap).
- **`_reasoning-log/`** — spent reasoning (session distillations), out of the default load path, read by its
  `index.md`. The **trace-to-source** layer: each distillation compiles up into `CONTEXT.md` and can be
  audited back. Most Reasoning Workspaces grow one.

## LOAD ORDER

ROOT CLAUDE.md (auto) → ROOT CONTEXT.md → Markets CLAUDE.md → Markets CONTEXT.md → this file →
this project's CONTEXT.md. For a production run, instead enter at the relevant factory's `CLAUDE.md`.

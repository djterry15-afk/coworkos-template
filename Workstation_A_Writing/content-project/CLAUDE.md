# CLAUDE.md
*Project: content-project — Writing workstation. Kind · State: **Reasoning · Active.***
*Read ROOT CLAUDE.md → Writing CLAUDE.md before reading this.*

---

## WHAT THIS PROJECT IS

*(Example.)* The standing strategy for what you publish and why: positioning, audience, the durable voice.
This is the **configure-the-factory** reasoning that feeds the tier-4 content factory's craft config. The
project does **not** draft pieces — that is the factory's job, one seed at a time.

## WHERE THINGS LIVE

- **`CONTEXT.md`** — the live synthesis: current positioning, strategy, any open thesis. Read it for state.
- **`content-factory/`** — the tier-4 workflow (staged-pipeline + hub). Enter at its own `CLAUDE.md` in
  production mode; it is self-contained and does **not** load this project's synthesis at run time.
- **`_reasoning-log/`** — spent reasoning (strategy/positioning distillations), out of the default load path,
  read by its `index.md`. The **trace-to-source** layer: each distillation compiles up into `CONTEXT.md`.
- **`references/`** — *reserved* — created only when a settled cross-run rule earns separation from state.
  (Here it stays empty: this project's settled craft lives downstream in the factory's `_config/`. Contrast
  Markets' `market-thesis/`, which *does* earn a `references/` — the folder is earned, not automatic.)

## LOAD ORDER

ROOT CLAUDE.md (auto) → ROOT CONTEXT.md → Writing CLAUDE.md → Writing CONTEXT.md → this file →
this project's CONTEXT.md. For a production run, instead enter at `content-factory/CLAUDE.md`.

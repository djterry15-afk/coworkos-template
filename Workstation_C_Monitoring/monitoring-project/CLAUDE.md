# CLAUDE.md
*Project: monitoring-project — Monitoring workstation. Kind · State: **Reasoning · Active.***
*Read ROOT CLAUDE.md → Monitoring CLAUDE.md before reading this.*

---

## WHAT THIS PROJECT IS

*(Example.)* Owns the **standing manifest** — the judgment of *which* metrics to monitor and *why* — which
is decided once (and revised rarely). The tier-4 monitor beneath it runs that manifest forever. Any
interpretation of the readings is reasoning that happens here (or upstream), never in the pipeline.

## WHERE THINGS LIVE

- **`CONTEXT.md`** — the live synthesis: what the manifest is watching and the rationale behind the metric
  set. Read it for state.
- **`stress-monitor/`** — the tier-4 workflow (deterministic monitor). Fetches data → transforms (pure) →
  renders a dated report; self-contained, does **not** load this project's synthesis at run time.
- **`references/`** — *reserved* — created only when a settled rule earns separation from state.

## LOAD ORDER

ROOT CLAUDE.md (auto) → ROOT CONTEXT.md → Monitoring CLAUDE.md → Monitoring CONTEXT.md → this file →
this project's CONTEXT.md. For a run, instead enter at `stress-monitor/CLAUDE.md`.

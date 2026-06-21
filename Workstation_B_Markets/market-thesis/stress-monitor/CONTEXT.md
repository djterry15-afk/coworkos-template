# CONTEXT.md — Market-Stress Monitor run router (L1)
*Pure standing config — this file does NOT change per run (run-state is naming + folder position).*
*Read `CLAUDE.md` first.*

---

## What a run is

One run = one **date**. Pull the standing manifest's metrics from FRED → snapshot → compute →
render a dated dashboard → glance. The metrics never change run-to-run; only the data refreshes.
That invariance is the point: this is the deterministic archetype.

## Where you are in a run

| If this exists… | …you are at |
|---|---|
| nothing for `<date>` | **00_plan** — confirm the standing manifest (light gate) |
| `01_fetch/snapshots/<date>/` | 01 done → run **02_transform** |
| `02_transform/computed/<date>.json` | 02 done → run **03_render** |
| `03_render/output/<date>/dashboard.md` | done → **glance** (the light review gate) |

## The two gates (both light)

1. **00 manifest gate** — approve the standing manifest *before* fetch. On a steady-state run this
   collapses to "manifest unchanged → go." It only does real work when a metric is added/changed
   (a logic decision — yours).
2. **03 glance gate** — read the dashboard. There is no heavy judgment here (that is the test that
   this is the *light-gate* archetype); the thesis call is separate, in the parent market-thesis project `CONTEXT.md`.

## Hard rule

No hard gate is needed (read-only / additive), but the run must stay self-contained: do **not**
load `../CONTEXT.md` during a run, and emit the load log. See `CLAUDE.md` §Self-containment.

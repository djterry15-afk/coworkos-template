# CLAUDE.md — content-factory
*Tier-4 WORKFLOW (pipeline-ICM), nested under the parent content project. Kind · State: **Pipeline · v2 (seed model).***
*L0 map of the factory. Read `CONTEXT.md` (the stage router) next, not the project's synthesis.*
*Archetype: the **content-production (staged-pipeline + hub)** shape — one of the three tier-4 workflow shapes the template demonstrates. See `00_Resources/references/tier-4-workflow-model.md`.*

---

## WHAT THIS IS

A self-contained ICM pipeline that takes **one post idea (a seed)** and produces **one publish-ready post.** It does **not** receive a finished angle — the pipeline **discovers the angle** from the material it pulls, with the human setting it at the `01_collect` gate. Reasoning about *what the tier-3 strategy is* stays at **tier-3 (the parent content project)**; the factory owns planning, research, and rendering. Human review gate at every stage; **hard gate before publish** (the factory never posts).

## PIPELINE

```
[tier-3: a seed idea] → 00_plan → 01_collect → 02_draft → 03_adapt → [hard gate] publish (external — out of scope)
```

- `_config/` — **craft config (HOW to render), standing:** `voice-core.md` (platform-neutral voice) + a slim `positioning.md` (who's-speaking stub). Per-platform voice lives in `03_adapt/references/`. The **WHAT** (the topic) arrives per run as a **seed**; the **angle** is set inside the pipeline.
- `00_plan/` — **take the seed → plan the run → manifest.** Scope what to pull (declared) and where to search (exploratory). **No idea-reasoning, no angle.**
- `01_collect/` — **fetch declared + discover exploratory sources** → local snapshot (verbatim) + **extract signal moments**, then **set the angle at the gate** (the U-curve peak).
- `02_draft/` — **execute the chosen angle** (`01`'s `direction.md`) into a platform-neutral core. Human edits *craft*, not the angle.
- `03_adapt/` — **THE HUB.** Renders the core to any platform in the seed's `platform-intent`; add a platform later by re-running with its voice config — no tier-3 trip. v2: LinkedIn populated; Skool seam reserved.

## WHERE THINGS LIVE (the category split)

| Job | Lives | Changes per run? |
|---|---|---|
| HOW to render (voice, craft) | factory `_config/` + `03_adapt/references/` | no |
| WHAT to explore (the seed / topic) | **tier-3** (stated, or the Skeleton / `content-briefs/`), pulled in | yes (per seed) |
| The ANGLE | discovered in-pipeline, set at the `01` gate (`direction.md`) | yes (per run) |
| Run-state | naming + folder position (no `RUNS.md`) | n/a |
| Finished runs | `_archive/<slug>/` | — |

## HARD RULES

- **Reasoning at tier-3, rendering here — but the angle is discovered *in* the pipeline, not handed down.** The factory never decides *what the tier-3 strategy is*; it does set the post's angle from the material, at the `01` gate.
- **Campaign ≠ post.** A campaign is a rare tier-3 act that emits a batch of seeds; the normal input is one idea. The factory runs one seed at a time.
- **Two modes of fan-in:** *declared* (known file, deterministic fetch) + *exploratory* (search a scope to discover sources). Both honor the **six guards** (see `01_collect/CONTEXT.md`); read-only on every source; a **live** source is a stop-and-reconsider.
- **Platform = intent (seed) + on-demand render (hub).** Never auto-route; render eligible platforms when asked.
- **Publish writes external permanent state → hard gate.** The factory halts at publish-ready.
- **Names are proposals** — renaming is cheap, not a redesign.

## STATUS

Seed model. The pipeline takes one seed → `00_plan` → exploratory + declared fan-in at `01` → angle set at the `01` gate → draft → adapt → publish-ready. Key design points it encodes: `00` = a mandatory scope stop; `01` = discovered-set + fidelity + angle (the U-curve peak); a source-authorship filter at `01` (your words vs retained AI output); the hub (`03_adapt`) renders the platform-neutral core to one or more sinks. v1 of this example renders one platform (LinkedIn); the second-platform seam (`03_adapt/references/voice-skool.md`) is **reserved** so adding a sink later changes only that file. Doctrine: `00_Resources/references/tier-4-workflow-model.md`.

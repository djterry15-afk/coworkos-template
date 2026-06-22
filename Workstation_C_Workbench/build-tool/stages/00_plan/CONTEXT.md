# CONTEXT.md — 00_plan (Layer-2 stage contract)
*A stage dispatcher in the pipeline-ICM body. Small (~a few hundred tokens). Scoped per stage at run time.*
*(Example stage — the link-checker build. Replace with your build's real stages.)*

---

## What this is
The build's planning gate: confirm the recipe and scope this build **before** any code is written. Mirrors
the other pipelines' `00_plan` — judgment is front-loaded here so the later stages can run cleanly.

## Inputs
- `../../references/recipe.md` — what to build and the constraints it obeys.
- The project `CONTEXT.md` build-state (what's already done).

## Process
1. Read the recipe; confirm it's still the intended build — or amend it (that edit *is* the configure act).
2. Scope this build: which functions, what's in v1 vs. deferred.
3. Write the plan for the run.

## Outputs
- `output/plan.md` — the scoped build plan for this run.

## GATE — light, before 01_build
Approve the recipe + scope. Changing the recipe here is direction-setting; the human signs off before code
is written.

## What NOT to do
- Don't write code here — this stage scopes the build, it doesn't perform it.

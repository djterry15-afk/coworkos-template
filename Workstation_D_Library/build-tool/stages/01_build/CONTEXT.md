# CONTEXT.md — 01_build (Layer-2 stage contract)
*A stage dispatcher in the pipeline-ICM body. Small (~a few hundred tokens). Scoped per stage at run time.*
*(Placeholder stage — shows the shape. Replace with your build's real stages.)*

---

## What this is
A single build stage. In a real Build/Workflow project, **your actual code/repo lives at this level** —
e.g. a `repo_vault/<your-repo>/` beside this contract, or the build scripts for this stage. The template
ships only the contract shape, not toy code to maintain.

## Inputs
*(What this stage consumes — the recipe from `../../references/recipe.md`, prior stage `output/`, source files.)*

## Process
*(What this stage does — the build step. Deterministic joints are scripts; judgment steps are human-gated.)*

## Outputs
*(What it produces → `output/`. Every output is an edit surface.)*

## What NOT to do
*(Out-of-scope actions; anything that needs a hard gate, e.g. publishing/deploying.)*

# CONTEXT.md — 01_build (Layer-2 stage contract)
*A stage dispatcher in the pipeline-ICM body. Small (~a few hundred tokens). Scoped per stage at run time.*
*(Example stage — the link-checker build.)*

---

## What this is
The stage that writes the code. **In a real Build/Workflow project, your actual repo lives at this level** —
e.g. `repo_vault/linkcheck/` beside this contract. The template ships the contract *shape*, not toy code to
maintain.

## Inputs
- `../00_plan/output/plan.md` — the approved scope.
- `../../references/recipe.md` — the conventions + hard constraints the code must obey.

## Process
1. Implement the recipe: link extraction (parse `[text](path)`), resolution (relative to each file's own
   directory), and the CLI entrypoint.
2. Keep the core **pure** (text + base path in, results out) so `02_test` can exercise it without the
   filesystem.
3. Human reviews **craft** — not whether to build, but whether the code is sound.

## Outputs
- The artifact — the `linkcheck` source in `repo_vault/` (real project). Every file is an edit surface.

## What NOT to do
- Don't add scope the plan didn't approve (no URL / wikilink checking in v1).
- Don't let the core read the filesystem directly — keep it pure, or `02_test` can't reach it.

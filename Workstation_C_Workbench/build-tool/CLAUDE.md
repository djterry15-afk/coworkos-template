# CLAUDE.md — build-tool
*Project: build-tool — Workbench workstation. Kind · State: **Build / Workflow · Active.***
*Read ROOT CLAUDE.md → Workbench CLAUDE.md before reading this.*

---

## WHAT THIS PROJECT IS

A project whose purpose is to **produce running code / artifacts** — an app, a script, a service. This is
the kind to use when you wrap ICM around an **actual codebase**.

A Build/Workflow project is **half this standard**:
- Its **project tier** (`CLAUDE.md` · `CONTEXT.md` · `references/`) is a **reasoning shell** — it follows
  the project conventions, holds the design state and the recipe, and is where you reason about the build.
- Its **body** (`stages/`, or a `repo_vault/` holding the actual repo) is **pipeline-ICM** (Layer 2 stage
  contracts + Layer 4 artifacts) — the code itself.

Don't confuse this with a Reasoning Workspace that *grew* a tier-4 production arm: here, the artifact
production *is* the project, not a downstream of a reasoning effort.

## WHERE THINGS LIVE

- **`CONTEXT.md`** — build-state + architecture decisions (the reasoning shell's synthesis).
- **`references/`** — the recipe handed down to the build (configure-the-factory input): constraints,
  conventions, the spec the code obeys.
- **`stages/`** — the pipeline-ICM body: a four-stage build pipeline `00_plan → 01_build → 02_test →
  03_release`, each a Layer-2 `CONTEXT.md` dispatcher with an `output/` (created on run). *(In a real project
  the actual code/repo lives at the build stage — e.g. `stages/01_build/repo_vault/<your-repo>/`.)*
- **`_reasoning-log/`** — *reserved.* This build's design reasoning currently lives inline in `CONTEXT.md`
  (ARCHITECTURE DECISIONS). It graduates to a `_reasoning-log/` once design sessions accumulate — as the
  larger live Build/Workflow projects do. Earned by accumulation, not created empty.

## PIPELINE (the `stages/` body)

```
00_plan        →   01_build        →   02_test          →   03_release
(confirm recipe     (write the code)    (verify vs.           (package + publish)
 + scope)                                fixtures)
  [GATE: light]       [review craft]      [GATE: on results]    [GATE: HARD — external write]
```

Example build: `linkcheck`, a markdown link-checker CLI (`references/recipe.md`). Plan → build → verify →
release, with the **hard gate on release** (publishing writes durable external state) — the same rule the
content factory applies at its publish step.

## LOAD ORDER

ROOT CLAUDE.md (auto) → ROOT CONTEXT.md → Workbench CLAUDE.md → Workbench CONTEXT.md → this file →
this project's CONTEXT.md → (for a build) the relevant stage's `CONTEXT.md`.

# CLAUDE.md — build-tool
*Project: build-tool — Library workstation. Kind · State: **Build / Workflow · Active.***
*Read ROOT CLAUDE.md → Library CLAUDE.md before reading this.*

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
- **`stages/`** — the pipeline-ICM body. Each stage has a Layer-2 `CONTEXT.md` dispatcher and an `output/`.
  *(In a real project this is where your actual code/repo lives — e.g. a `repo_vault/<your-repo>/`.)*

## LOAD ORDER

ROOT CLAUDE.md (auto) → ROOT CONTEXT.md → Library CLAUDE.md → Library CONTEXT.md → this file →
this project's CONTEXT.md → (for a build) the relevant stage's `CONTEXT.md`.

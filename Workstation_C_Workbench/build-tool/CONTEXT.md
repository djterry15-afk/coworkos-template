# CONTEXT.md
*Project: build-tool — the reasoning shell's synthesis (build-state + architecture decisions).*

> **STOP:** read this project's `CLAUDE.md` before this file.

---

## CURRENT STATE

*(Placeholder — your real build-state lives here.)* What's built, what's in progress, what's blocked. The
architecture decisions and their rationale. This is the shell you reason in; the code lives in `stages/`.

## ARCHITECTURE DECISIONS

*(Placeholder.)* The load-bearing choices and why — kept here so the build doesn't drift from its design.

## THE BODY

`stages/` (or a `repo_vault/<your-repo>/`) holds the actual code. The reasoning happens here at the project
tier; the code is built there. At build time the relevant context from this shell is distilled into the
stage contracts once, and a build run scopes context per stage.

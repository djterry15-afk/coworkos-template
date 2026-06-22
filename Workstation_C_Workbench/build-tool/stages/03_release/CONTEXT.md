# CONTEXT.md — 03_release (Layer-2 stage contract)
*A stage dispatcher in the pipeline-ICM body — the deliverable hand-off.*
*(Example stage — the link-checker build.)*

---

## What this is
Package the verified artifact into the deliverable — a tagged release / published package. This is where the
build leaves the workspace.

## Inputs
- The tested artifact (green from `02_test`).
- `../02_test/output/test-report.md` — the evidence it passed.

## Process
1. Version + package the artifact.
2. Write release notes (what it does, how to run it).
3. Publish / tag — **only after the hard gate**.

## Outputs
- `output/<version>/` — the packaged release + notes.

## GATE — HARD (this writes external, permanent state)
Releasing publishes durable state outside the workspace — the bounded-autonomy rule requires a **hard gate**.
The pipeline halts at release-ready; the human approves the publish. (Same rule as the content factory's
publish step — a second, different context where "external write → hard gate" applies.)

## What NOT to do
- Don't publish on green tests alone — the human gates the external write.
- Don't release an artifact with a red or skipped test.

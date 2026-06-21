# CLAUDE.md
*Workstation: Monitoring — an EXAMPLE domain for recurring data-monitoring.*
*Read ROOT CLAUDE.md fully before reading this. Read this fully before any project files.*

---

## WHAT THIS WORKSTATION IS FOR

*(Example.)* The domain where you watch a recurring data stream and want a dated, legible report each run —
no fresh reasoning per run, just refreshed data against a standing set of metrics. The tier-4 deterministic
monitor beneath the project does the repetition; the human glances at the output.

---

## PROJECT MAP

**monitoring-project** — `Reasoning · Active`. Owns the standing manifest (which metrics matter and why),
plus a tier-4 deterministic monitor (data → transform → report) that produces a dated dashboard on demand.
→ Folder: `monitoring-project/`

---

## ROUTING TABLE

| Task | Navigate to | Load | Skip |
|---|---|---|---|
| Deciding/revising which metrics to monitor | monitoring-project/ | This file + CONTEXT.md → project files | — |
| Running the monitor (a dated run) | monitoring-project/stress-monitor/ | the factory's own files (production mode) | project synthesis |

---

## NAVIGATION SEQUENCE

1. ROOT CLAUDE.md (done) → 2. ROOT CONTEXT.md → 3. this file → 4. Monitoring CONTEXT.md →
5. the project's CLAUDE.md + CONTEXT.md → 6. begin work.

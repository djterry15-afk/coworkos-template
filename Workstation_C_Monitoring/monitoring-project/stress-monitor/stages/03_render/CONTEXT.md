# 03_render — Render the Dashboard (L2 stage contract)
*One job: format the computed readings into the markdown dashboard. A deterministic joint → glance gate.*

---

## What this is

The third mechanical joint and the deliverable. `render.py` formats `computed/<date>.json` into the
dashboard per `_config/dashboard-format.md`. It adds no numbers and no interpretation — every value
traces to the computed file (hence to the snapshot).

---

## Contract

| | |
|---|---|
| **Input** | the latest `02_transform/computed/<date>.json` |
| **Also load** | `_config/dashboard-format.md` (the schema) |
| **Skip** | FRED · the snapshot internals · the parent thesis `CONTEXT.md` |
| **Output** | `03_render/output/<date>/dashboard.md` (+ the run's `load-log.md`) |

---

## Process

`python stages/03_render/render.py` → writes the dashboard. Then write `load-log.md` for the run
(every file/endpoint opened) so self-containment is falsifiable.

---

## GATE (light, glance) — the review

Read the dashboard. This is the *light* gate — no heavy judgment here. If a reading warrants action,
that is **input to your reasoning**: take it to the parent research project `CONTEXT.md`. The dashboard never concludes.

---

## What NOT to do

- No verdict, no signal, no alarm threshold (thresholds don't transfer across episodes).
- Never add a number not present in the computed file.

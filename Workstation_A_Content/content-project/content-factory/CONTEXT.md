# CONTEXT.md — content-factory stage router
*L1 dispatcher (~300 tokens). **NOT a synthesis.** Production mode: scope per stage; do not reload the project's reasoning synthesis.*

---

## RUN-MODE LOADING

This is a **production run**, not reasoning navigation. Entry = this router. Load `_config/` **once** (`voice-core` + the slim `positioning` stub — *craft only*), then the **active stage's** `CONTEXT.md` and its inputs only. The run's input is a **seed** (a topic, not an angle), captured at `00_plan`; the **angle is discovered in-pipeline** and set at the `01` gate. Do **not** reload the parent content project synthesis; fan-in fetches only the declared/discovered settled files.

## WHERE AM I → WHAT TO LOAD

| Stage | Job | Load |
|---|---|---|
| `00_plan` | Take the seed → plan the run → manifest | `00_plan/CONTEXT.md` + `manifest-schema.md` + the seed (and any named backlog item) |
| `01_collect` | Fetch declared + discover exploratory → snapshot + extract → **set angle** | `01_collect/CONTEXT.md` + the manifest |
| `02_draft` | Execute the chosen angle → platform-neutral core | `02_draft/CONTEXT.md` + `direction.md` + `signal-moments.md` + `_config/voice-core.md` + `positioning.md` |
| `03_adapt` | Render eligible platform(s) on demand | `03_adapt/CONTEXT.md` + `references/voice-<platform>.md` + the core draft |

## RUN STATE — naming + folder position (no ledger)

**This router is standing config — it never changes per run.** Run-state is read from the files: a `00_plan/output/manifest-<slug>.md` exists → that run started; the furthest stage `output/` holding `<slug>` → its current gate. No central ledger.

To start a run: a **seed** (one idea) is given at entry — stated directly, or picked from a tier-3 backlog (`LinkedIn Content Skeleton.md` / `content-briefs/`); `00_plan` captures it and writes the manifest. On completion, a run's working files move to **`_archive/<slug>/`** so the active stage folders hold only in-flight work.

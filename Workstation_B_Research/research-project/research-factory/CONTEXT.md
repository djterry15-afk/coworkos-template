# CONTEXT.md — Research Factory Router (L1)
*Pure standing config. Never changes per run — run-state lives in the files (see CLAUDE.md).*
*You are running the pipeline. This routes you to the active stage. Read that stage's
CONTEXT.md, do its one job, stop at its gate.*

---

## Which stage am I at?

For the run's `<slug>`:
- no `00_plan/manifest-<slug>.md` → **00_plan**
- manifest exists, no `01_source/<slug>/sources-<slug>.md` ledger → **01_source** (discover phase)
- ledger exists, no `01_source/<slug>/snapshot-*.md` → **01_source** (at the gate → commit snapshots on approval)
- snapshots exist, no `02_extract/evidence-<slug>.md` → **02_extract**
- evidence exists, no `03_synthesize/output/brief-<slug>.md` → **03_synthesize**
- brief accepted → archive `<slug>` working files → `_archive/<slug>/`, done

---

## What to load per stage — the Skip column matters more than Load

| Stage | Load | Skip |
|---|---|---|
| 00_plan | this file · `stages/00_plan/CONTEXT.md` · `_config/reliability-bar.md` | the wiki · the web · `artifact-format.md` · downstream stages |
| 01_source | `stages/01_source/CONTEXT.md` · `_config/reliability-bar.md` · `_config/provenance-rules.md` · `../llm-wiki/wiki/index.md` | **`../CONTEXT.md` (thesis synthesis)** · downstream contracts |
| 02_extract | `stages/02_extract/CONTEXT.md` · this run's snapshots + `sources-<slug>.md` | the web (no re-fetch) · the wiki · _config craft already applied |
| 03_synthesize | `stages/03_synthesize/CONTEXT.md` · `_config/artifact-format.md` · this run's `evidence-<slug>.md` | the raw snapshot (work from extracted evidence) · other runs · thesis synthesis |

---

## The gates — where the human decides

- **00 → 01:** approve the question framing · the scope · any declared sources. **Mandatory stop.**
- **01 (U-curve peak, mid-stage):** approve the **candidate ledger** — source set · grades · angle —
  **before** any snapshot is committed. No autonomous scope-narrowing. Full/raw snapshots of approved
  sources are captured only after sign-off.
- **02 → 03:** confirm extracted evidence **faithfully matches** the snapshot.
- **03 → done:** confirm the brief represents the graded evidence and **stops short of a verdict.**

---

## What NOT to do

- Don't load the parent thesis synthesis (`../CONTEXT.md`). Self-contained by design.
- Don't write to the wiki. The pipeline's terminus is the brief.
- Don't issue a verdict. Evidence in, evidence out — the operator concludes.

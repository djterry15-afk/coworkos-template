# CLAUDE.md — Market-Stress Monitor (tier-4 workflow)
*Pipeline-ICM workflow nested under the parent research project.*
*WORKFLOW tier — an artifact-producing pipeline. Output: one dated stress-dashboard report per run.*
*Archetype: the **deterministic / mechanical-joint** shape — one of the three tier-4 workflow shapes the
template demonstrates (the others: a content pipeline+hub, and exploratory-fan-in research). Real scripts
at the joints, two light gates, no hard gate; standing-manifest config, not a per-run seed. It is runnable
out of the box against the free FRED API (supply your own key — see `.env.example`). Doctrine:
`../../../00_Resources/references/tier-4-workflow-model.md`.*

---

## What this is

The **determinism-heavy archetype**: a recurring `data → transform → report` monitor. It pulls a
**standing set** of FRED-native financial-stress metrics, computes current readings + historical
context, and renders a markdown dashboard. **Scripts do the repetition; the human gates lightly.**

The **acquire→monitor seam**: an upstream research step (the research-factory archetype) *found which*
plumbing metrics lead; **this factory monitors them** on a schedule. It does **not** conclude — readings +
context in, a glance out; the thesis call stays in the parent research project `CONTEXT.md`.

**Defining trait vs. the other two tier-4s: the manifest is STANDING config**
(`_config/manifest.json` — the same metrics every run), not a per-run seed. "Spend intelligence
designing the manifest once, run determinism forever."

---

## Pipeline shape

```
00_plan          →   01_fetch         →   02_transform       →   03_render
(confirm manifest)    (FRED → snapshot)    (compute — pure)       (computed → dashboard)
  [GATE: light —        (fetch.py)           (transform.py)         (render.py)  [GATE: glance]
   approve manifest]
```

Two **light** gates only: approve the standing manifest at **00** (changes rarely), glance the
dashboard at **03**. The middle (01→02→03) is pure determinism — no gate between. **No hard gate:**
the pipeline is read-only / additive — it fetches public data and writes only into its own
`output/`. It never writes external state or human-authored content. (Contrast the content
factory's publish step, which *is* a hard gate.)

---

## Folder structure

```
stress-monitor/
├── CLAUDE.md            ← this map (L0)
├── CONTEXT.md           ← run router (L1) — pure standing config
├── HOW-TO-RUN.md        ← operator onboarding
├── requirements.txt     ← fredapi + pandas (infrastructure — taken, not built)
├── _config/             ← L3 standing config — the configure-once intelligence
│   ├── manifest.json    ← THE STANDING MANIFEST (series + metrics) — machine-readable, authoritative
│   ├── manifest.md      ← the manifest's rationale (why these metrics) + the 00-gate note
│   ├── fetch-rules.md   ← key handling, snapshot + provenance rules
│   └── dashboard-format.md  ← the 03_render output schema
└── stages/
    ├── 00_plan/CONTEXT.md
    ├── 01_fetch/CONTEXT.md      + fetch.py      (+ snapshots/<date>/ per run)
    ├── 02_transform/CONTEXT.md  + transform.py  (+ computed/<date>.json per run)
    └── 03_render/CONTEXT.md      + render.py     (+ output/<date>/dashboard.md per run)
```
*Per-run `snapshots/`, `computed/`, and `output/` folders are created on run, not before.*

---

## Run-state = naming + position (no ledger)

"The system is the memory." No RUNS.md, no ACTIVE pointer — `CONTEXT.md` and `_config/` are pure
standing config and never change per run.
- A run is one **date** (`YYYY-MM-DD`, the run day).
- Started ⟺ `01_fetch/snapshots/<date>/` exists. Current position ⟺ the furthest stage holding a
  `<date>` artifact.
- Complete ⟺ `03_render/output/<date>/dashboard.md` exists and has been glanced. Dated outputs
  **accumulate** in `output/` — that history *is* the record (like a `posts/` archive); no separate
  `_archive/`. Old raw snapshots may be pruned; the rendered report is the keeper.

---

## Self-containment — the boundary that keeps a run cheap

At run time load **only**: ROOT `CLAUDE.md` (auto) + ROOT `CONTEXT.md` (operator contract) + these
factory files + the active stage + this run's own artifacts.

- **DON'T** read `../CONTEXT.md` (the parent project's synthesis) during a run. Monitoring the
  metrics must not depend on the thesis it informs.
- **One-directional, read-only.** The pipeline reads FRED and writes only into its own folders. It
  never writes the wiki, the parent, or the web.
- The scripts touch **only** FRED + the local snapshot — self-contained by construction.
- **Emit a load log at run start** (`output/<date>/load-log.md`) — every file/endpoint opened — so
  self-containment is *falsifiable*.

---

## Naming

| Artifact | Path |
|---|---|
| Standing manifest | `_config/manifest.json` (+ `_config/manifest.md` rationale) |
| Raw snapshot + provenance | `01_fetch/snapshots/<date>/<SERIES_ID>.csv` + `provenance.json` |
| Computed readings | `02_transform/computed/<date>.json` |
| Dashboard (the deliverable) | `03_render/output/<date>/dashboard.md` |
| Load log | `03_render/output/<date>/load-log.md` |

---

## Run-time read order

ROOT `CLAUDE.md` (auto) → ROOT `CONTEXT.md` → **this file** → `CONTEXT.md` → the active stage's
`CONTEXT.md`. If you've never driven this factory, read `HOW-TO-RUN.md` first.

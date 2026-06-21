# CLAUDE.md — Research Factory (tier-4 workflow)
*Pipeline-ICM workflow nested under the parent market-thesis project.*
*WORKFLOW tier — an artifact-producing pipeline. Output: one source-grounded research brief per run.*
*Archetype: the **exploratory fan-in / research-acquisition** shape — one of the three tier-4 workflow
shapes the template demonstrates (the others: a content pipeline+hub, and a deterministic monitor). Seed →
discover + grade external evidence → research brief, human-gated throughout. Use it as a starting skeleton:
keep the four-stage shape and the gates, replace the `_config/` craft with your own reliability bar.*

*Capture note: when a source can't be captured (timeout / 403 / paywall), it is **dropped, never
paraphrased** from a search summary — no snapshot, not evidence. A network-level failure differs from a
tool failure: the fallback is a different **source class** (e.g. an official review that reports the
figure), not a different scraping tool. See `_config/provenance-rules.md`.*

---

## What this is

The **acquisition front-end the llm-wiki lacks.** It takes one research question (a *seed*),
goes and finds reliable **external** evidence, and produces a **research brief** — evidence
laid out, graded, provenance-stamped. It does **not** decide the thesis.

The three roles stay separate (the acquire-vs-organize cut):
- **This pipeline *acquires*** — finds and grades new external evidence → a brief.
- **The `../llm-wiki/` *organizes*** — stores and links sourced data (consulted here, never written by here).
- **the operator *concludes*** — reasons over the brief → the verdict lands in the parent market-thesis project `CONTEXT.md`.

---

## Pipeline shape

```
00_plan      →   01_source                     →   02_extract     →   03_synthesize
(seed→manifest)  (discover+grade →GATE→ snapshot)   (raw→evidence)     (evidence→brief)
   [gate]            [GATE — peak, mid-stage]          [gate]             [gate]
```

Human gate at every stage. The heavy one is **01_source** — the U-curve peak, where the operator
approves the candidate source set + reliability grades **before** any snapshot is committed.

---

## Folder structure

```
research-factory/
├── CLAUDE.md            ← this map (L0)
├── CONTEXT.md           ← run router (L1) — pure standing config
├── HOW-TO-RUN.md        ← operator onboarding (provisional — refine after first run)
├── _config/             ← L3 craft, stable across runs
│   ├── reliability-bar.md
│   ├── provenance-rules.md
│   └── artifact-format.md
└── stages/
    ├── 00_plan/CONTEXT.md       (+ manifest-<slug>.md per run)
    ├── 01_source/CONTEXT.md     (+ <slug>/ snapshots + sources-<slug>.md per run)
    ├── 02_extract/CONTEXT.md    (+ evidence-<slug>.md per run)
    └── 03_synthesize/CONTEXT.md (+ output/brief-<slug>.md per run)
```
*`_archive/<slug>/` and the per-run `output/` folders are created when earned, not before.*

---

## Run-state = naming + position (no ledger)

"The system is the memory." There is **no RUNS.md and no ACTIVE pointer** — `CONTEXT.md`
and `_config/` are pure standing config and never change per run.
- A run is one **slug** (kebab-case of the question).
- Started ⟺ `00_plan/manifest-<slug>.md` exists. Current gate ⟺ the furthest stage folder
  holding a `<slug>` artifact.
- On completion (brief accepted into the parent market-thesis project `CONTEXT.md`): archive the run's working
  files → `_archive/<slug>/`.

---

## Self-containment — the boundary that keeps a run cheap

At run time load **only**: ROOT `CLAUDE.md` (auto) + ROOT `CONTEXT.md` (operator contract)
+ these factory files + the active stage + this run's own artifacts.

- **DO** read `../llm-wiki/` via its `index.md` — scoped, Layer-3-style. That is the organized
  *source store* (the precheck at 01), not synthesis.
- **DON'T** read `../CONTEXT.md` (the parent project's synthesis). Producing the brief must
  not depend on the conclusion it feeds.
- **One-directional, read-only.** The pipeline never writes to the wiki, the web, or the parent.
  Wiki ingestion of the brief's sources is a *separate, downstream* act.
- **Emit a load log at run start** — list every file opened — so self-containment is *falsifiable*.

---

## Naming

| Artifact | Path |
|---|---|
| Manifest | `00_plan/manifest-<slug>.md` |
| Snapshots + graded ledger | `01_source/<slug>/` + `01_source/<slug>/sources-<slug>.md` |
| Evidence | `02_extract/evidence-<slug>.md` |
| Brief (the deliverable) | `03_synthesize/output/brief-<slug>.md` |
| Completed run | `_archive/<slug>/` |

---

## Run-time read order

ROOT `CLAUDE.md` (auto) → ROOT `CONTEXT.md` → **this file** → `CONTEXT.md` → the active stage's
`CONTEXT.md`. If you've never driven this factory, read `HOW-TO-RUN.md` first.

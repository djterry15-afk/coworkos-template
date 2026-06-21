# Tier-3 (Project) Model
*ROOT Layer-3 reference. How to organize files **within a project**. Load when setting up or reorganizing
a project. The cross-tier foundation (tiers vs layers, the recurrence rule, the three axes) lives in
`tier-1-2-root-workstation-model.md` — load that for the model itself; this applies it at the project tier.*

---

## The principle

A project folder is organized **one home per content-nature** — and each nature maps to an ICM layer. The
failure mode this prevents is *mixing every nature into one undifferentiated context*, which forces the
model (and you) to sort 30 files to find the 2 that matter. Separate by nature and context arrives
already-organized; the default load path stays clean.

Carry one thing down from the foundation: a layer is a *job a file does*, not a tier you climb. A reasoning
project has L0 (`CLAUDE.md`) and L1 (`CONTEXT.md`) and may have L3 (`references/`, a wiki); L2 and L4
appear only when it grows a `stages/` workflow beneath it (tier 4).

---

## Project kinds & lifecycle — classify before you structure

Before applying any home-mapping, classify the project on **two independent axes**.

**Axis 1 — KIND (what motions it runs):**

| Kind | Motions | What it gets |
|---|---|---|
| **Reasoning Workspace** | all four — ingest external → reason → synthesize to `CONTEXT.md` → archive spent thinking | the **full four-home model** |
| **Reference Repo** | one reference-motion. *External*-authored = wiki-nature (sources you consult); *own*-authored = `references`-nature (records/rules you keep) | the **lighter Reference-Repo spec** |
| **Build / Workflow** | produces running code / artifacts | **half this standard** — its project tier is a *reasoning shell* that follows these conventions; only the code/artifact body (e.g. `stages/`) is pipeline-ICM (Layer 2+4) |

**Telling Reasoning from Reference is ICM's Layer 3/4 axis, one level up.** *What is your relationship to
the project's core content?* You **consult / internalize** it → Layer-3 nature → **Reference Repo.** You
**process it as input to produce synthesis** → Layer-4 nature → **Reasoning Workspace.** Classify on the
*relationship*, not the content's appearance — two folders of external material can be opposite kinds.

**Axis 2 — STATE (aliveness):** `Forming (stub)` → `Active` → `Dormant (promotable)` → `Dead (superseded)`.

**State gates structure; kind shapes it.** Nothing earns its home structure until it is **Active**. A
Forming or Dormant project gets `CLAUDE.md` + `CONTEXT.md` at most (often just a holding folder) — imposing
the full model early is the empty-ceremonial-folder trap. When a dormant project reactivates, it promotes
into its kind's structure *then*.

**Standardize *toward* the kinds — reshape a misfit to the nearest kind, don't mint a new kind.** New kinds
carry a high bar: a project must run a genuinely different *motion* than the three here (consult /
synthesize / produce-artifacts), not merely look unusual.

---

## Folder skeletons by kind

`[opt]` = present only when earned. **State gates all of it.**

**Reasoning Workspace**
```
project/
├── CLAUDE.md          map + kind tag
├── CONTEXT.md         live synthesis — the center (sized by relevance)
├── references/        [opt] EXTRACTED settled rules — often thin/empty pre-execution
├── llm-wiki/          [opt] only if it ingests external sources (index.md · log.md · pages)
├── _reasoning-log/    spent thinking, trace-to-source (index.md = control point)
└── logs/              [opt] pure operational run-records
```

**Reference Repo · external**
```
project/
├── CLAUDE.md          map (may double as the control point)
├── CONTEXT.md         routing / orientation — NOT a synthesis (thin; or absent)
└── <body, by topic>/  control point = index.md OR a content map in CONTEXT.md
                       deep repos nest CLAUDE.md + CONTEXT.md per subfolder
```

**Reference Repo · own, active (template-shaped)**
```
project/
├── CLAUDE.md          doubles as the reference BODY — the schema you obey
├── README.md          outward-facing instantiation doc (sits in the CONTEXT.md slot)
├── LICENSE            if published
└── <scaffold>/        the instantiable structure
```

**Build / Workflow**
```
project/               ← reasoning shell (follows THIS standard)
├── CLAUDE.md          map + load order
├── CONTEXT.md         build-state + architecture decisions
├── references/        the recipe handed down (configure-the-factory input)
└── stages/            ← pipeline-ICM body (Layer 2+4) — see tier-4-workflow-model.md
```

---

## Layer → home mapping

| Content nature | Home | ICM layer | Loaded |
|---|---|---|---|
| Map — "where am I, what's here" | `CLAUDE.md` | Layer 0 | every session |
| Synthesized current truth | `CONTEXT.md` | Layer 1 | every session |
| Stable rules / conventions | `references/` | Layer 3 | by trigger |
| External source knowledge, read-*from* | `llm-wiki/` | Layer 3 (loading) / 4 (nature) | by trigger |
| Spent reasoning / trace-to-source | `_reasoning-log/` | spent Layer 4 | rarely, by index |
| Forward context to the next session | handoff file (root) | — | consumed, then deleted |

---

## Adoption menu (criteria, not mandate)

*Applies once a project is a **Reasoning Workspace**.* A slot exists only when content earns it; empty
ceremonial folders are the over-engineering trap.

- **`CLAUDE.md` + `CONTEXT.md`** — every project. The two primitives.
- **`references/`** — when the project has *settled* constraints worth separating from current state.
  Detailed-but-unsettled exploration is not a constraint — it stays in `CONTEXT.md`.
- **`llm-wiki/`** — **only when the project ingests external source material** it reads repeatedly. Most
  projects don't; default is no wiki.
- **`_reasoning-log/`** — when session distillations and notes accumulate. Most reasoning projects qualify.

---

## The `_reasoning-log/` archive

**What it is:** your own session distillations, superseded snapshots, and loose notes — already-digested
thinking (*spent Layer 4*, compiled into `CONTEXT.md`).

**Why keep it:** trace-to-source. When `CONTEXT.md` sounds wrong, trace back to the reasoning that produced
a conclusion and fix it there.

**Why it sits out of the default load path:** spent artifacts are read rarely. The underscore prefix sorts
it out of primary navigation. Read it by its `index.md`, not in bulk.

---

## Sizing `CONTEXT.md` — relevance, not a token budget

The project synthesis is sized by *holistic relevance*: it holds what a session needs to reason well, and
no spent detail that belongs in `_reasoning-log/`. It is the one place real synthesis lives (the
router→synthesis→router bulge). Keep conclusions current — the truth layer must never lag the work.

---

## The fourth tier — where workflows live

A project grows a **WORKFLOW (tier 4)** beneath it once its **Layer 3 is stable enough to hand to a
script** — the reasoning → production transition. The project tier stays a reasoning shell (this standard);
the workflow body is pipeline-ICM (Layer 2 stage contracts + Layer 4 per-run artifacts). At build time the
parents' relevant context is distilled **once** into the factory's L3 config; at run time the factory reads
its own config and does **not** reload the parent synthesis. See `tier-4-workflow-model.md`.

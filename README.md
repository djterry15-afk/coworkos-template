# CoworkOS — an ICM workspace template

A file-based template for running cross-domain work with an AI coding agent (built for
[Claude Code](https://claude.com/claude-code), but the structure is plain markdown + folders, so it
ports). The **structure is the system**: routing tables decide what context loads, plain-text files are
the memory, and human gates govern anything that writes durable state.

It is a denatured skeleton — replace the example workstations with your own domains.

## The architecture: CoworkOS + ICM

Instead of one giant context window (or RAG at query time), context is organized into a tree of small,
purpose-scoped files. Each node has a **map** (`CLAUDE.md`) and a **router/synthesis** (`CONTEXT.md`); the
agent navigates the tree and loads only what the current task needs. Two ideas are welded together:

- **CoworkOS**: a four-level **tier tree** that separates context by scope — `ROOT → WORKSTATION → PROJECT → WORKFLOW` (with domain workstations and project kind/state rules).
- **ICM (Interpretable Context Methodology)**: applied at Tier 4 (Workflow), a **five-layer model** (L0 map · L1 route/synthesis · L2 stage contract · L3 reference · L4 artifacts) that says *what job each file does* and *how little to load at once*.

The key correction the model makes: **a tier is a place, a layer is a job — they are orthogonal.** Full
write-up in [`00_Resources/references/tier-1-2-root-workstation-model.md`](00_Resources/references/tier-1-2-root-workstation-model.md).

## Structure

```
CLAUDE.md / CONTEXT.md          ROOT — map + operator contract (auto-loaded every session)
00_Resources/references/        the doctrine: tier-1-2, tier-3, tier-4 models + design rationale
Workstation_A_Writing/          example domain → content-project → content-factory (one shape)
Workstation_B_Markets/          example domain → market-thesis, one COMPOSED project:
                                  llm-wiki (organizes) + research-factory (fan-in) + stress-monitor (monitor)
Workstation_C_Workbench/        example domain holding two MIXED-KIND projects:
                                  reference-library (Reference Repo) + build-tool (Build/Workflow)
```

The template demonstrates **two orthogonal taxonomies**, arranged to show how the system really composes:

- **Project kinds** (*what a project is*, tier-3): **Reasoning Workspace** (Writing, Markets) · **Reference
  Repo** · **Build/Workflow** (the last two live side by side in Workbench).
- **Workflow shapes** (*how a tier-4 pipeline is wired*, tier-4): the three below.

The three example domains show **composition**, not a flat catalog:

- **Writing** — the simple case: one project, one shape.
- **Markets** — the composed case: one `market-thesis` project runs the whole **acquire → organize → monitor
  → conclude** loop (a fan-in research factory + a deterministic monitor + a wiki, all under one project).
  *A shape is a property of a workflow, not a domain.*
- **Workbench** — the mixed-kind case: one domain, two projects of different kinds. *A kind is a property of
  a project, not a domain.*

The skeleton (the tier wiring + conventions) is the canon; the examples are fillings. Replace them with your
own domains.

## The three tier-4 (WORKFLOW) shapes

A tier-4 is a numbered-stage pipeline that produces artifacts, built beneath a project once its reference
layer is stable. The three shapes span the space:

| Shape | Motion | Example |
|---|---|---|
| **Content production** (staged-pipeline + hub) | seed → collect → draft a platform-neutral core → render to N platform sinks | `content-factory` |
| **Research acquisition** (exploratory fan-in) | seed → discover + grade external sources → snapshot → evidence brief | `research-factory` |
| **Deterministic monitor** | standing manifest → fetch data → transform → dated report | `stress-monitor` |

Doctrine: [`00_Resources/references/tier-4-workflow-model.md`](00_Resources/references/tier-4-workflow-model.md).
Each pipeline ships with one small **illustrative sample run** (in its `_archive/` or `output/`) so you can
see the shape end-to-end.

## The core rules

- **Determinism over intelligence.** Spend intelligence designing the structure once; let a script run the
  repetition. Never leave an LLM in a loop a script could run.
- **AI advises, human decides, system executes.** Judgment lives at gates; determinism lives at mechanical
  joints. Anything that writes external/permanent state gets a **hard gate**.
- **The angle is set in-pipeline, not handed down.** The tier-3 → tier-4 handoff is a *seed* (a topic), not
  a finished answer — the pipeline discovers the angle from the material at its first gate.
- **Snapshot, don't navigate.** A pipeline fetches declared sources into a local snapshot and reads that;
  it doesn't reach live into other parts of the tree at run time.

## Getting started

1. Open this folder in your agent. ROOT `CLAUDE.md` loads automatically and routes from there.
2. Rewrite ROOT `CONTEXT.md` — the **operator contract** (who you are, how you want the agent to work). The
   `WHO I AM` / `HOW I WORK` sections are placeholders; the operating principles and protocols are the
   system's design philosophy.
3. Replace the example workstations with your own domains, following the tier-1-2 and tier-3 models.
4. To see a tier-4 run live, try the deterministic monitor — it works out of the box:

```bash
cd Workstation_B_Markets/market-thesis/stress-monitor
cp .env.example .env          # then put your free FRED API key in .env
pip install -r requirements.txt
python stages/01_fetch/fetch.py
python stages/02_transform/transform.py
python stages/03_render/render.py
# → stages/03_render/output/<date>/dashboard.md
```

(Get a free FRED API key at <https://fred.stlouisfed.org/docs/api/api_key.html>. The monitor pulls public
financial-stress series; swap the manifest for any recurring data stream you care about.)

## License

MIT — see [LICENSE](LICENSE).

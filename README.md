# CoworkOS — an ICM workspace template

A file-based template for running cross-domain work with an AI coding agent (built for
[Claude Code](https://claude.com/claude-code), but the structure is plain markdown + folders, so it
ports). The **structure is the system**: routing tables decide what context loads, plain-text files are
the memory, and human gates govern anything that writes durable state.

It is a denatured skeleton — replace the example workstations with your own domains.

## The idea: ICM (Intelligent Context Management)

Instead of one giant context window (or RAG at query time), context is organized into a tree of small,
purpose-scoped files. Each node has a **map** (`CLAUDE.md`) and a **router/synthesis** (`CONTEXT.md`); the
agent navigates the tree and loads only what the current task needs. Two ideas are welded together:

- a **tier tree** that separates context by scope — `ROOT → WORKSTATION → PROJECT → WORKFLOW`;
- the **ICM five-layer model** (L0 map · L1 route/synthesis · L2 stage contract · L3 reference · L4
  artifacts) that says *what job each file does* and *how little to load at once*.

The key correction the model makes: **a tier is a place, a layer is a job — they are orthogonal.** Full
write-up in [`00_Resources/references/tier-1-2-root-workstation-model.md`](00_Resources/references/tier-1-2-root-workstation-model.md).

## Structure

```
CLAUDE.md / CONTEXT.md          ROOT — map + operator contract (auto-loaded every session)
00_Resources/references/        the doctrine: tier-1-2, tier-3, tier-4 models
Workstation_A_Content/          example domain → content-project → content-factory (tier-4)
Workstation_B_Research/         example domain → research-project → research-factory (tier-4)
Workstation_C_Monitoring/       example domain → monitoring-project → stress-monitor (tier-4)
```

The three workstations each demonstrate **one tier-4 workflow shape**. The skeleton (the tier wiring +
conventions) is the canon; the pipelines are fillings that show the range.

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
cd Workstation_C_Monitoring/monitoring-project/stress-monitor
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

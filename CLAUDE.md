# CoworkOS — Workspace Map
*Auto-loaded every session. Map only — structure, routing, navigation.*
*This is a denatured template. Replace the example workstations/projects with your own.*

---

## What This Is

A tiered, file-based **Intelligent Context Management (ICM)** workspace for cross-domain reasoning
and artifact production with an AI agent. The structure *is* the system: routing tables decide what
to load, plain-text files are the memory, and human gates govern anything that writes durable state.

Tiers: **ROOT → WORKSTATION → PROJECT → (WORKFLOW when a project matures)**.
Each tier has `CLAUDE.md` (L0 map + L1 routing) and `CONTEXT.md` (orient / current state).
At ROOT, `CONTEXT.md` also carries the **operator contract** (who you are, how you want the agent to
work, reliability/failure/memory protocols).

Architecture foundation: `00_Resources/references/tier-1-2-root-workstation-model.md`.

---

## Folder Structure

```
coworkos-template/
├── CLAUDE.md                          ← this file — auto-loaded every session (L0 map + L1 routing)
├── CONTEXT.md                         ← ROOT operator contract + current state — load every session
├── README.md                         ← outward-facing: what this template is + how to instantiate
├── 00_Resources/                     ← cross-workstation reference layer
│   └── references/                   ← Layer 3 — stable reference, load by trigger
│       ├── tier-1-2-root-workstation-model.md   ← architecture foundation + ROOT/WORKSTATION conventions
│       ├── tier-3-project-model.md   ← how to organize files within a project
│       └── tier-4-workflow-model.md  ← the WORKFLOW (pipeline-ICM) tier model + the three shapes
├── Workstation_A_Content/            ← EXAMPLE — a content/writing domain
│   └── content-project/
│       └── content-factory/          ← tier-4 pipeline: content-production (staged-pipeline + hub)
├── Workstation_B_Research/           ← EXAMPLE — a research/analysis domain
│   └── research-project/
│       └── research-factory/         ← tier-4 pipeline: research-acquisition (exploratory fan-in)
└── Workstation_C_Monitoring/         ← EXAMPLE — a recurring-monitoring domain
    └── monitoring-project/
        └── stress-monitor/           ← tier-4 pipeline: deterministic monitor (data → transform → report)
```

The three workstations demonstrate one tier-4 **shape** each — they are fillings that show the range;
the skeleton (the tier wiring + conventions) is the canon. Replace them with your real domains.

---

## Routing Table

| Task | Navigate to | Load | Skip |
|------|-------------|------|------|
| Content / writing work | Workstation_A_Content/ | Workstation CLAUDE.md + CONTEXT.md → project files | B, C |
| Research / analysis | Workstation_B_Research/ | Workstation CLAUDE.md + CONTEXT.md → project files | A, C |
| Monitoring / recurring data | Workstation_C_Monitoring/ | Workstation CLAUDE.md + CONTEXT.md → project files | A, B |
| Cross-workstation prioritization | ROOT only | CLAUDE.md + CONTEXT.md | All workstation files |
| Architecture / ICM decisions | 00_Resources/references/ | tier-1-2-root-workstation-model.md | All workstation files |
| Setting up / reorganizing a project | 00_Resources/references/ | tier-3-project-model.md | All workstation files |
| Building a tier-4 workflow under a project | 00_Resources/references/ | tier-4-workflow-model.md + tier-3-project-model.md | All workstation files |
| Ambiguous — domain unclear | Ask before navigating | One clarifying question | — |

*ROOT-only boundary: if the task is **what to work on** across workstations, stay at ROOT. If it is
**doing work** within a domain, navigate down.*

---

## Navigation Sequence

1. ROOT `CLAUDE.md` — auto-injected at session start (this file). Done.
2. Read ROOT `CONTEXT.md` — the operator contract + current state.
3. Identify the workstation from the routing table.
4. Read that workstation's `CLAUDE.md` then `CONTEXT.md` — both.
5. If a specific project is in play, read its `CLAUDE.md` then `CONTEXT.md` — both.
6. Only then begin work.

Navigate without being prompted when the routing target is clear. When it isn't — ask one clarifying
question before navigating.

---

## Environment

Fill in your own: OS · languages · editor · agent. Workspace root: this folder.

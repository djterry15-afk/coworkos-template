# CoworkOS — Workspace Map
*Auto-loaded every session. Map only — structure, routing, navigation.*
*This is a denatured template. Replace the example workstations/projects with your own.*

---

## What This Is

A tiered, file-based workspace applying the **Interpretable Context Methodology (ICM)** for cross-domain reasoning
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
│   ├── cross-domain-map.md           ← L1 orient — links across workstations; load for cross-domain questions
│   └── references/                   ← Layer 3 — stable reference, load by trigger
│       ├── tier-1-2-root-workstation-model.md   ← architecture foundation + ROOT/WORKSTATION conventions
│       ├── tier-3-project-model.md   ← how to organize files within a project (the project KINDS)
│       ├── tier-4-workflow-model.md  ← the WORKFLOW (pipeline-ICM) tier model + the three SHAPES
│       ├── decisions-log.md          ← the design rationale (the "why" behind the template's shape)
│       ├── icm-paper.md              ← distillation of the ICM source paper (Van Clief & McDermott)
│       ├── karpathy-llm-wiki.md      ← distillation of the LLM Wiki pattern (Karpathy) the wiki uses
│       └── skills/                   ← invokable procedures (session close, handoff, build spec, web capture)
├── Workstation_A_Writing/            ← EXAMPLE domain (subject-area) — the simple case: one project, one shape
│   ├── content-project/              ← Reasoning Workspace
│   │   └── content-factory/          ← tier-4 shape: content-production (staged-pipeline + hub)
│   └── forming-idea/                 ← STATE example — a Forming stub (kind undetermined; structure not yet earned)
├── Workstation_B_Markets/            ← EXAMPLE domain — the COMPOSED case: one project runs the whole loop
│   └── market-thesis/                ← Reasoning Workspace — acquire → organize → monitor → conclude
│       ├── llm-wiki/                 ← organizes sourced knowledge (Layer-3 store)
│       ├── research-factory/         ← tier-4 shape: research-acquisition (exploratory fan-in) — acquires
│       └── stress-monitor/           ← tier-4 shape: deterministic monitor (data → transform → report)
└── Workstation_C_Workbench/          ← EXAMPLE domain — the MIXED-KIND case: contrasting kinds side by side
    ├── reference-library/            ← Reference Repo — FLAT: consult / retrieve entries one at a time
    ├── reference-study/              ← Reasoning Workspace (study container) — synthesize ACROSS reference sub-projects
    ├── build-tool/                   ← Build / Workflow — reasoning shell over a code body
    └── retired-tool/                 ← STATE example — a Dead own-reference (finished, retired; structure shed)
```

The template demonstrates **three orthogonal axes** — two at tier-3: project **kind** (Reasoning Workspace ·
Reference Repo · Build/Workflow — *what a project is*) and project **state** (Active · Forming · Dead —
*whether it's alive; state gates structure*); plus the tier-4 **shape** (staged-pipeline+hub · exploratory
fan-in · deterministic monitor — *how a pipeline is wired*). They're arranged to show **composition**, the
way the system is really used:
- **Writing** is the simple case: one project, one shape (a content factory).
- **Markets** is the composed case: a single `market-thesis` project runs the full **acquire → organize →
  monitor → conclude** loop — two different tier-4 shapes (fan-in research + deterministic monitor) plus a
  wiki, under one project. *A shape is a property of a workflow, not of a domain.*
- **Workbench** is the mixed-kind case: one domain holding projects of contrasting kinds — a **flat Reference
  Repo** (`reference-library`, consult one entry at a time), a **Reasoning Workspace** that *synthesizes
  across* reference sub-projects (`reference-study` — the material is still reference material; the
  *relationship* makes the container Reasoning), and a **Build/Workflow** (`build-tool`). *A kind is a property
  of a project, not of a domain — and `reference-library` vs `reference-study` puts the two opposite
  relationships to reference material side by side.*

All three kinds and all three shapes are present, and the **state** axis is shown by the two examples that
exist to teach it — `forming-idea` (Forming/stub) and `retired-tool` (Dead) — demonstrating *state gates
structure* at the two ends of the lifecycle (structure not-yet-earned vs. structure shed). The skeleton — the
tier wiring + conventions — is the canon; these examples are fillings. Replace them with your real domains.

---

## Routing Table

| Task | Navigate to | Load | Skip |
|------|-------------|------|------|
| Content / writing work | Workstation_A_Writing/ | Workstation CLAUDE.md + CONTEXT.md → project files | B, C |
| Research, analysis, or monitoring a thesis | Workstation_B_Markets/ | Workstation CLAUDE.md + CONTEXT.md → market-thesis files | A, C |
| Reference lookup / building a tool | Workstation_C_Workbench/ | Workstation CLAUDE.md + CONTEXT.md → the relevant project | A, B |
| Cross-workstation prioritization | ROOT only | CLAUDE.md + CONTEXT.md | All workstation files |
| Question spanning two or more domains | ROOT + cross-domain map | CLAUDE.md + CONTEXT.md + `00_Resources/cross-domain-map.md` → the project files its rows point to | Unrelated project files |
| Architecture / ICM decisions | 00_Resources/references/ | tier-1-2-root-workstation-model.md (+ decisions-log.md for the "why") | All workstation files |
| Setting up / reorganizing a project | 00_Resources/references/ | tier-3-project-model.md | All workstation files |
| Building a tier-4 workflow under a project | 00_Resources/references/ | tier-4-workflow-model.md + tier-3-project-model.md | All workstation files |
| Session close / distillation | 00_Resources/references/skills/ | distillation.SKILL.md | Everything else |
| Handoff to next AI session | 00_Resources/references/skills/ | session-handoff.SKILL.md | Everything else |
| End of exploration / ready to build | 00_Resources/references/skills/ | build-protocol.SKILL.md | Everything else |
| Capturing web content (posts, archives, gated pages) to files | 00_Resources/references/skills/ | web-capture.SKILL.md | Everything else |
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

## Skills

Invokable procedures — load the file when its trigger fires, not before.

| Skill | Trigger | Location |
|-------|---------|----------|
| distillation | Session close — reasoning clears the keep-it bar | `00_Resources/references/skills/distillation.SKILL.md` |
| session-handoff | Work continues in a new chat | `00_Resources/references/skills/session-handoff.SKILL.md` |
| build-protocol | End of exploration, ready to write a build spec | `00_Resources/references/skills/build-protocol.SKILL.md` |
| web-capture | A web corpus (posts, archives, gated pages) needs capturing to files | `00_Resources/references/skills/web-capture.SKILL.md` |

---

## Environment

Fill in your own: OS · languages · editor · agent. Workspace root: this folder.

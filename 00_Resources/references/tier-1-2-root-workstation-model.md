# Tier-1-2 (ROOT & Workstation) Model — and the Cross-Tier Foundation
*ROOT Layer-3 reference. The structural foundation the tier-3 and tier-4 specs rest on, plus the
conventions for the thin ROOT/WORKSTATION router tiers. Load when reasoning about the architecture itself,
defining a tier, or deciding where a file or convention belongs.*

---

## Provenance — two source systems, welded

This workspace combines two systems that were never designed together:

- **The tier tree** — a simple folder/routing template: `ROOT → WORKSTATION → PROJECT`, with a *map* and
  a *router* at each node. A **navigation** system that separates context by scope.
- **The five layers — from ICM** (Interpretable Context Methodology): a 0–4 context-role
  model for a **single sequential pipeline** — numbered stages, human review gates, produces artifacts. A
  **context-engineering** system concerned with *what job each file does* and *how little to load at once*.

The two fuse cleanly only once you reject the tempting wrong assumption — **that tier *N* is ICM layer
*N***. It isn't. Tiers and layers are orthogonal axes. Untangling that is the point of this document.

---

## Tiers are places; layers are jobs

- **A tier is a *place*** — a node in the folder tree you *navigate* (ROOT → WORKSTATION → PROJECT →
  WORKFLOW). The number is **depth of scope**: how global the place is (ROOT = everything → WORKFLOW = the
  task in hand).
- **A layer is a *job a file does*** — ICM's 0–4 context roles. A file *is* a layer the way a tool *is* a
  hammer; you don't move between them. The number is **specificity of context**, not execution order.

**You do not climb layers by climbing tiers.** Each tier re-instantiates the same small set of
layer-jobs, scoped down. "Who am I / where do I go" recurs at ROOT, at each WORKSTATION, at each PROJECT —
that is not redundancy, it is the fractal.

---

## The four tiers (places)

The top three are **reasoning-ICM** — a tree navigated by routing table; output is synthesized truth and
decisions. The fourth is **pipeline-ICM** — the classic numbered-stage workflow; output is artifacts.

| Tier | Scope | Carries (layers) |
|---|---|---|
| **ROOT** | the whole workspace | L0 map + L1 routing (+ L3 resources) |
| **WORKSTATION** | one domain | L0 map + L1 routing (+ L3 resources) |
| **PROJECT** | one effort | L0 + L1 **synthesis** **+ L3 recipe** (`references/`, a wiki) |
| **WORKFLOW** | one repeatable pipeline | **L2 stage-contract + L4 artifacts** |

The seam is the **PROJECT** tier: a navigation node that also carries ICM's Layer 3 (the recipe). The
**WORKFLOW** tier is the only place the full five-layer pipeline appears. ROOT and WORKSTATION are pure
router tiers; they borrow only L0 + L1.

---

## The five layers (jobs)

| Layer | File | Question | Job |
|---|---|---|---|
| **L0** | `CLAUDE.md` | "Where am I?" | identity + map |
| **L1** | `CONTEXT.md` | "Where do I go?" | routing (at router tiers) / synthesis (at project tier) |
| **L2** | stage `CONTEXT.md` | "What do I do?" | stage contract (Inputs/Process/Outputs) |
| **L3** | reference material | "What rules apply?" | the recipe / config — stable across runs |
| **L4** | working artifacts | "What am I working with?" | the product — per-run |

The ICM pipeline has **one** L0/L1 pair, then `stages/`. This workspace **replicates the L0/L1 pair at
every node** of the tier tree — routing recursing inside scope.

---

## The weld — how tiers carry layers

**Recurrence rule:** **L0, L1, and L3 recur at every reasoning tier. Only L2 (stage contract) and L4
(per-run artifact) are workflow-exclusive** — they exist only inside a `stages/` pipeline. L3 reference
appears at ROOT (`00_Resources/`), at WORKSTATION (`references/`), and at PROJECT (`references/`, a wiki).

**The L1 mutation — router → synthesis.** In the pipeline, L1 is a small **router** ("which stage handles
this"). The router tiers keep that, but at the **project tier L1 mutates into a *synthesis*** — a digest
of current truth you reason over, sized by relevance, not a token budget. A pipeline needs a dispatcher; a
reasoning space needs a cache of comprehension.

**The shape that falls out — router → synthesis → router:**

| Tier | `CONTEXT.md` form | Holds |
|---|---|---|
| ROOT / WORKSTATION | **router** | scoped "who I am / how to engage" + cross-cutting state that spans children |
| PROJECT | **synthesis** | the live digest you reason over (the one place real synthesis lives) |
| WORKFLOW (stage) | **router/contract** | L2 dispatcher, back to the small budget |

The synthesis **bulges in the middle**. Demote rule: *everything that belongs to one child routes down;
only what spans children stays.* This is why the upper tiers must stay thin — making ROOT/WORKSTATION rich
syntheses is the over-engineering trap.

---

## Three orthogonal axes (don't conflate them)

A file's placement is set by three independent questions:

1. **Nature → which home.** What job does the content do? (map / orient / reference / source / spent
   thinking) → content-nature picks the folder. *One home per nature.*
2. **Token-load → splitting *within* a layer.** Less irrelevant context = better, so a single
   always-loaded layer is split into lean files. A loading optimization, **not** a nature boundary.
3. **Routing → load-timing.** The routing table decides *what loads when*. Because the router controls
   loading, doc granularity should follow **nature**, not load-timing — anything can be routed in on demand.

**Why ROOT bundles L0+L1 into `CLAUDE.md`, freeing `CONTEXT.md` for the operator contract.** At a
reasoning ROOT there are no stages to route to — the table routes to *workstations* — so `CLAUDE.md`
carries both L0 (map) and L1 (routing). That frees `CONTEXT.md`. ICM has **no operator layer** (it is an
artifact pipeline, no human collaborated *with*), so this workspace adds one: the **operator contract**
(who you are, how to collaborate, the reliability/failure/memory protocols) lives in ROOT `CONTEXT.md`
alongside cross-cutting state. The "who I am / how to engage" job **recurs down the router tiers** — at
WORKSTATION it reappears scoped down as the *domain posture delta*.

---

## ROOT & WORKSTATION tier conventions

Both are pure router tiers (L0 + L1 + L3 reference, never L2/L4). Both split their two always-loaded files:

- **`CLAUDE.md` = "where I am"** — L0 map + L1 routing, collapsed into one file: scope, child map, routing
  table, navigation.
- **`CONTEXT.md` = "who I am / how to engage + cross-cutting state"** — the role ICM has no layer for.

The "who" content is scoped by tier; the demote rule governs it — *only the delta over the parent is kept:*

- **ROOT `CONTEXT.md`** carries the **global** "who" — the operator contract + current cross-domain state.
- **WORKSTATION `CONTEXT.md`** carries the **domain delta** — how to show up in *this* domain + genuine
  cross-project tensions. **Move-and-dedupe:** never re-state what ROOT already says.

**Synthesis stays thin; posture is not synthesis.** A workstation `CONTEXT.md` is full to the degree its
domain has posture worth stating and its projects genuinely interact; a domain with neither may have a
near-empty `CONTEXT.md`, and that is correct.

**No per-project roll-call.** The stable **kind·state tag** (`Active` / `Dormant` / `Paused`) lives in the
`CLAUDE.md` PROJECT MAP — the routing anchor. Volatile per-project *progress* lives only in that project's
own `CONTEXT.md`. A status roll-call at the workstation tier duplicates state and drifts.

**`references/` is created only when a cross-project constraint actually settles** — not created empty (the
empty-ceremonial-folder trap; state gates structure).

**The PROJECT tier is the deliberate exception to the who/where split:** "who I am" has already been
supplied by the two router tiers above via load order, so the project `CONTEXT.md` is freed from the
who-job and mutates into the live **synthesis**. See `tier-3-project-model.md`.

---

## Where this sits among the guidance docs

- **This file** — the cross-tier foundation + the ROOT/WORKSTATION conventions. Load to reason about
  *structure*.
- **`tier-3-project-model.md`** — the deep spec for the PROJECT tier (the homes, kind × state, triage).
- **`tier-4-workflow-model.md`** — the pipeline-ICM (workflow-tier) spec + the three workflow shapes.
- **ROOT `CONTEXT.md`** — the operator contract + current cross-cutting state.

# Tier-4 (Workflow) Model — the pipeline-ICM tier
*ROOT Layer-3 reference. The WORKFLOW tier — the one place the full five-layer numbered-stage pipeline
appears, built beneath a project once its Layer 3 is stable. Load when building a tier-4 workflow. The
cross-tier foundation lives in `tier-1-2-root-workstation-model.md`; the project seam it hangs under is in
`tier-3-project-model.md`.*

---

## What the workflow tier is

Tiers 1–3 are *reasoning-ICM* — a tree navigated by routing table; output is synthesized truth and
decisions. The fourth tier is *pipeline-ICM* — the classic numbered-stage workflow; **output is
artifacts**. It is the only tier that carries **L2 (stage contract) + L4 (per-run artifact)**; everything
above borrows only L0/L1/L3. A project grows a workflow beneath it once its **Layer 3 is stable enough to
hand to a script** — the reasoning → production transition.

Where it sits: **one reasoning parent → nest it as the project's fourth-tier subfolder** (canonical);
**multiple parents → graduate it to a workstation-level home.**

---

## The five durable findings

**1. Tier-4 is pure ICM — principles vs. properties.** ICM's design *principles* (one-stage-one-job ·
plain-text interface · layered context loading · every-output-an-edit-surface · configure-the-factory)
**define** purity. *Portability / self-containment are properties of the hand-off examples, not
principles* — you may relax portability (if you don't hand the factory off) without losing anything that
defines ICM.

**2. ICM = judgment-at-gates + determinism-at-mechanical-joints** — *not* deterministic-only. Pipelines
alternate: **plan / extract / draft / align = judgment** (human gates); **fetch / format / publish =
deterministic** (scripts). "Spend intelligence designing, run determinism forever" applies *per joint*. A
step that writes external permanent state (publish) carries a **hard gate**.

**3. Two optional, *earned* capabilities — fan-in and fan-out.** Baseline tier-4 = a **closed** pipeline
(self-contained inputs, one output). Add **input fan-in** (declare cross-tree sources, fetch them in) and
**output fan-out** (one stream forks to many sinks) only when a workflow earns it (state gates structure).
Most workflows have neither.

**4. Configure-the-factory (tier-3, once) / plan-the-run (tier-4 stage 00) boundary.** Tier-3 configures
the factory once (the craft/voice/rules → the factory's **L3 config**). Tier-4 `00_plan` plans each run
(which item · which sinks · which sources) → the **manifest**, which *is* the ICM Inputs table keyed by the
run. A fetch script is then a pure function of its manifest. *(The angle/answer is **not** pre-decided at
tier-3 — it is set in-pipeline at the collect/source gate; see "the seed.")*

**5. Input fan-in "done right" = six guards** (each an existing principle on the input boundary):
1. **Conditional** — declared only when a workflow needs external sources.
2. **One declared manifest** — one inspectable throat, not deep paths scattered through stages.
3. **Fetch → local snapshot** — stages read the snapshot, never reach out live (reproducible).
4. **One-directional, read-only** — fan-in never writes back to a source (hard gate).
5. **Provenance-stamped** — records what was pulled, from where, when.
6. **Point at stable / snapshotted sources** — not another project's mid-flight synthesis.
Enforced at the heaviest review gate: review the manifest *before* fetch, then the extracted signal
*against* the snapshot.

---

## Categorize tier-4s by workflow *shape*, not domain

Three shapes span the space (this template demonstrates one of each):

| Shape | Motion | Example in this template |
|---|---|---|
| **Staged pipeline + hub** (content-production) | seed → collect → draft platform-neutral core → render to N sinks | `Workstation_A_Content/.../content-factory` |
| **Exploratory fan-in** (research-acquisition) | seed → discover + grade external sources → snapshot → brief | `Workstation_B_Research/.../research-factory` |
| **Deterministic monitor** | standing manifest → fetch data → transform (pure) → render report | `Workstation_C_Monitoring/.../stress-monitor` |

**The discriminating test for the deterministic shape:** its value must live in the **determinism** (the
repetition a script runs forever) **and** its input must be **data, not reasoning-output** (so the
transform is genuinely pure and the gate is a glance). This rules out judgment-heavy "monitors" (a
conformance linter) and stream-less ones (a digest of frozen snapshots) — both are reasoning tools in a
deterministic costume.

**Defining traits that distinguish the shapes:**
- Content + research take a fresh **seed** every run. The monitor takes a **standing manifest** (config —
  the same inputs every run); on a steady-state run `00_plan` collapses to "confirm → go," and that
  collapse *is* the proof of the deterministic shape.
- **Acquire vs. organize vs. conclude.** A pipeline that *acquires* new external evidence is a tier-4. A
  store that *organizes* sourced knowledge (a wiki) is standing L3, not a pipeline. *Concluding* (a
  verdict) is the human's job, in `CONTEXT.md`. Keep the three separate; a pipeline that only organizes
  sources is wiki work, not a tier-4.

---

## The reasoning ↔ production seam — the seed

**The handoff object carries a *seed*, not a finished angle.** The tier-3 → tier-4 handoff is a **topic /
question / item** (+ optional source pointers + intent) — a research-brief, not a thesis. The pipeline owns
planning, research, and **angle-setting**; tier-3 does **not** pre-decide the angle. Pre-deciding it
amputates ICM's heaviest gate — the collect/source stage *is* the judgment peak precisely because the angle
is set *there, after the material surfaces it*. Fan-in is the angle-discovery engine; you cannot pre-decide
the angle and then pull the material meant to inform it.

**Two modes of fan-in:**
- **Declared** — the source is known; name it in the manifest, fetch deterministically.
- **Exploratory** — a seed drives a *search to discover* relevant sources, snapshotted once found. Discovery
  is judgment at run time — legitimate, because it is the research joint (a judgment gate). The manifest is
  **built during planning** (recording everything pulled), not handed in complete.

**Where the angle lives: the collect/source gate** (the U-curve peak). The human sets it there; the draft
stage executes it and the human edits *craft*. An angle still unresolved at draft = the extraction was thin
→ re-collect, not a tier-3 round-trip.

**Live vs. settled (guard 6).** Pull from *settled* sources (published work, finished narratives, archived
material, dormant project state). A **live** source — most sharply another project's mid-flight
`CONTEXT.md` — is a **stop-and-reconsider** at the gate: if you need live material, the thinking hasn't
settled, which is a reasoning signal, not a production input.

**Run-state = naming + folder position** (manifest exists → started; furthest stage folder → current
gate); no central ledger ("the system is the memory"). Archive a run on completion, out of the active stage
folders.

---

## Two loading modes (the tier-3 ↔ tier-4 seam)

Two context-load philosophies that do not fire at once:
- **Reasoning mode (tiers 1–3)** — load top-down ROOT → workstation → project to *find and think about*
  work; holistic synthesis.
- **Production mode (tier 4)** — *run* the pipeline; scope context **per stage** (a few thousand tokens per
  stage, vs a monolithic load).

The bridge: at **build** time the parents' relevant context is distilled **once** into the factory's L3
config; at **run** time the factory reads its own config and does **not** reload the parent synthesis.
**Input fan-in is therefore a *local fetch, not a navigation load*:** `00_plan` declares files,
`01` copies them to a snapshot, stages read the snapshot — the other trees are never navigated. This is why
nesting an ICM factory under a reasoning tree does not drown the run in context. A nested factory is a
**self-contained workspace** with its own L0 + L1 router, so a production run loads only the ROOT operator
contract + the factory's own files. Emit a **load log** at run start so self-containment is *falsifiable*.

---

## Stage anatomy

Each stage `CONTEXT.md` = *What This Is · What to Load (with a **Skip** column — it matters more than Load)
· Process · Skills (each with a **When** trigger) · What NOT to Do*, sized small (≈25–80 lines).
Naming-as-state on disk (`draft-v1 → v2 → final`, `<slug>` / `<date>` namespacing) — state on disk, no DB.
The platform/branch fork is a **human-decided branch at a gate**, never auto-routed (auto-branching would
turn ICM into a framework).

---

## Legibility is a deliverable

An artifact its own operator can't read has **failed**, even if the pipeline ran perfectly. Plain-language
framing and self-explaining output are within doctrine, not polish — especially for the deterministic
monitor, whose whole value is a human glancing at it and understanding it.

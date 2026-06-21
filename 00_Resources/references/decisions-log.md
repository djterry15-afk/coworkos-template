# Design Rationale & Decisions Log
*ROOT Layer-3 reference. The "why" behind this template's shape — read it to understand the design before
changing it, and append to it (dated) as the template evolves. This is the published repo documenting its
own architecture; it is **not** a copy of the source workspace's private build history.*

---

## What this template is distilled from

This template is a **denatured skeleton** lifted from a working ICM workspace and stripped of its owner's
personal content. The method was **copy-then-strip**: the live, validated structures were copied into a
clean repo, then all personal/domain content was removed and replaced with generic placeholders. Nothing
here is theoretical — every pattern shipped because it earned its place in real use first.

That history is intentionally *not* carried into this repo. The record of how the template was built belongs
to the workspace that produced it (the producer), not to the product. This file holds only the **durable
rationale** a new user or contributor needs.

---

## Core design decisions

**Tiers are places; layers are jobs — they are orthogonal.** The single most important correction the model
makes. Climbing the tier tree (ROOT → workstation → project → workflow) does **not** climb ICM layers; each
tier re-instantiates the same small set of layer-jobs, scoped down. See
`tier-1-2-root-workstation-model.md`.

**Two taxonomies, demonstrated through composition.** The template shows both — arranged the way the system
is really used (composed), not as a flat one-per-slot catalog:
- **Project *kinds* (tier-3):** Reasoning Workspace · Reference Repo · Build/Workflow — *what a project is*.
- **Workflow *shapes* (tier-4):** staged-pipeline+hub · exploratory fan-in · deterministic monitor — *how a
  production pipeline is wired*.

- **Writing** — the simple case: one Reasoning Workspace, one shape (a content factory).
- **Markets** — the composed case: a single `market-thesis` project runs the full acquire → organize →
  monitor → conclude loop — *two* tier-4 shapes (exploratory fan-in research + deterministic monitor) plus an
  organizing wiki, all under one project. A domain/project composes multiple shapes; **a shape is a property
  of a workflow, not of a domain.**
- **Workbench** — the mixed-kind case: one domain holding two projects of different kinds (Reference Repo +
  Build/Workflow); **a kind is a property of a project, not of a domain.**

Together: all three kinds and all three shapes, shown in composition.

**Why composition over a flat catalog (2026-06-21 restructure).** An earlier published draft used a
one-workstation-per-shape catalog (separate Content / Research / Monitoring domains + a Library domain for
the two leftover kinds). It was tidy but misrepresented the system: it named domains after *work-types* (a
"Monitoring" domain is a shape wearing a domain's clothes), hid the acquire → organize → monitor → conclude
seams the doctrine itself describes, and implied one-shape-per-domain. The restructure co-locates the
research factory + monitor + wiki under one market thesis (their real relationship), names domains as
subject-areas, and keeps the mixed-kind Workbench.

**Why three workflow shapes, validated before inclusion.** The three shapes span the space of how a tier-4
pipeline can be wired — produce-and-fan-out, acquire-by-discovery, and run-determinism-on-a-schedule. Each
was built and run on real work before being generalized; an unproven shape was never shipped as canon. The
**discriminating test** that admits the deterministic shape: its value must live in the *determinism* and
its input must be *data, not reasoning-output* — which rules out judgment-heavy or stream-less "monitors."

**Judgment at gates, determinism at mechanical joints.** ICM is not deterministic-only. Pipelines alternate
human-gated judgment steps with scripted deterministic ones; anything that writes external/permanent state
gets a **hard gate**.

**The seed, not the answer.** The tier-3 → tier-4 handoff carries a *topic/question* (a seed), never a
pre-decided angle. The pipeline discovers the angle from the material at its first gate (the judgment peak).
Pre-deciding it amputates the heaviest gate.

**Snapshot, don't navigate.** A pipeline fetches declared sources into a local snapshot and reads that; it
does not reach live into other parts of the tree at run time. This is why nesting a production factory under
a reasoning tree doesn't drown the run in context.

**State gates structure.** Folders and structure are created only when content earns them — never empty
ceremonial scaffolding. A Forming or Dormant project gets only `CLAUDE.md` + `CONTEXT.md`.

---

## Changelog

*(Append dated entries here as the template evolves — e.g. new examples, doctrine refinements.)*

- **Initial release.** ROOT + operator-contract template; the tier-1-2 / tier-3 / tier-4 doctrine; three
  Reasoning-Workspace workstations (one workflow shape each, with an illustrative sample run); a
  library/tooling workstation demonstrating the Reference Repo and Build/Workflow kinds.
- **2026-06-21 — restructured to composition.** Replaced the one-workstation-per-shape catalog with a
  composed layout: **Writing** (one project, one shape), **Markets** (`market-thesis` running fan-in research
  + a deterministic monitor + a wiki — the acquire → organize → monitor → conclude loop), **Workbench**
  (mixed-kind Reference Repo + Build/Workflow). Domains renamed as subject-areas; the research sample
  re-themed to a markets question ("which stress metrics lead vs. lag?") so it coheres with the monitor it
  feeds. All three kinds and three shapes retained.
- **2026-06-21 — monitor key-loading fix.** Added `python-dotenv` to the monitor's `requirements.txt` so the
  documented `.env` flow works out of the box (the `load_dotenv` import was optional and silently no-opped).

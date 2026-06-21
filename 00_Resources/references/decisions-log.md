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

**Two taxonomies, demonstrated deliberately.** The template shows both:
- **Project *kinds* (tier-3):** Reasoning Workspace · Reference Repo · Build/Workflow — *what a project is*.
- **Workflow *shapes* (tier-4):** staged-pipeline+hub · exploratory fan-in · deterministic monitor — *how a
  production pipeline is wired*.

Workstations A/B/C are Reasoning Workspaces, one workflow shape each. Workstation D is a single domain
holding two projects of the **other** two kinds (Reference Repo + Build/Workflow) — which also demonstrates
the truth that a workstation contains mixed-kind projects (a kind is a project-level property, not a
domain-level one). Together: all three kinds × all three shapes.

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

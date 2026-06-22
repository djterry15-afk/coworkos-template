# Cross-Domain Map
*ROOT-level connection layer (L1 orient). Load for any question that spans two or more workstations.*
*Holds links between domains — never content. The content lives in the project files the anchors point to.*

---

## What this is

A catalog of how reasoning in one domain connects to another, so a cross-domain
question can surface the relevant links and route to the right project knowledge
**without loading every project's CONTEXT.md or wiki**. The table is the index; the
anchors point into the project files where the actual content already lives.

This is the markdown-native cross-domain layer — the alternative to merging everything
into one wiki (which hits token limits) or leaving domains siloed (which buries the
connections). Token cost stays flat: a cross-domain question loads ROOT `CLAUDE.md`
(auto) + this file + only the one or two project files the relevant rows point to.

## Hard rules

- **Anchors point to current synthesized state only** — project `CONTEXT.md` files and
  wiki pages. **Never anchor to distillation / `_reasoning-log` files.** Those are a
  mutable reasoning log (context, not truth); the map must not inherit their staleness.
- **Connections live only here.** Project files don't duplicate the connection; a
  project's `CONTEXT.md` may *reference* a row when the link is load-bearing for it, but
  the catalog has one home — no two copies to drift apart.
- **Additive, provenance-tracked.** A row is born the moment a cross-domain link surfaces
  during real work — not from an upfront cataloging pass. The map accretes.

## How a row is born

During project work, when you (or the agent) notice that a conclusion in one domain
touches another, add a row here in the same pass — the same discipline as updating a
wiki's index and log on ingest.

---

## The Map

*The row below is an **example** using this template's example domains. Delete it and add
your own as real links surface.*

| Connection | Domains | The link (one line) | Anchors | Status |
|---|---|---|---|---|
| Thesis conclusion → content angle | Markets ↔ Writing | A settled verdict in `market-thesis` is the seed for a piece — the Writing factory turns a Markets conclusion into an explainer; the dependency runs Markets → Writing | `Workstation_B_Markets/market-thesis/CONTEXT.md` · `Workstation_A_Writing/content-project/CONTEXT.md` | example |

---

## Column key

- **Connection** — short name for the link.
- **Domains** — which workstations it bridges.
- **The link** — one line: how they connect, and which way the dependency runs.
- **Anchors** — clickable pointers into the *current-state* files on each side (`CONTEXT.md` / wiki pages only).
- **Status** — `live` (active link), `dormant` (real but not currently in play), `resolved` (closed out), `example` (template placeholder — replace).

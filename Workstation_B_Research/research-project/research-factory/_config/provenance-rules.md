# Provenance Rules — _config (L3, stable across runs)
*How 01_source snapshots and stamps a source. Implements fan-in guards 3 / 5 / 6:
fetch → local snapshot · provenance-stamped · settled sources.*

---

## Snapshot raw, post-approval

Every **approved** source is captured to a local snapshot — **full/raw** (the whole relevant source
text), so 02 curates from it and the gate-02 fidelity check verifies against the real source, not a
pre-selection. Stages 02/03 read the snapshot, never re-fetch. Reproducible: the brief can be
re-derived from the snapshot months later even if the URL rots.

**Snapshotting follows the 01 gate** — capture only the sources the operator approved (the durable snapshot follows approval:
capturing before approval is sunk cost and clutter).

**Pick the capture tool by the source:**
- **WebFetch → save** — discrete public page/PDF (right-sized; the common case).
- **web-capture skill** (browser/Playwright) — gated, JS-heavy, or WebFetch-blocked sites (e.g. an HTTP 403).

**Failed capture → exclude, never paraphrase.** If a source can't be captured (403 / paywall / JS) it is
**not evidence**: drop it (or hold as a lead) and re-grade without it. Never quote a search-result summary
in place of a snapshot. *(this discipline is a stage rule.)*

---

## Provenance stamp — every snapshot carries a header

- source title + author / institution
- URL / DOI / book + page, and **capture date**
- **GRADE** (A/B/C) and **AUTHORSHIP** tag (human-primary / ai-authored)
- source **STATE** (settled / live)
- **how it was found** (wiki precheck / web search / declared pointer / workspace) — the location axis

---

## One throat

All sources for a run are recorded in **one** manifest (`00_plan/manifest-<slug>.md`) and
snapshotted under `01_source/<slug>/`. No source enters from a side door — one inspectable
inventory per run.

---

## Read-only, one-directional

The pipeline never writes back to a source — not the web, not the wiki, not another project.
Snapshots are copies. The wiki ingesting the sources afterward is a **separate, downstream** act,
done by the operator / the wiki, not by this pipeline.

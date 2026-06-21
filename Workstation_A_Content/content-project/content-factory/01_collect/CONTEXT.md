# CONTEXT.md — 01_collect (stage contract)
*Job: pull the seed's sources (declared fetch + exploratory discovery) → snapshot + extract signal moments, then **set the angle** at the gate. This is the **U-curve peak** — the heaviest human gate, where direction is decided.*

---

## INPUTS
- The manifest from `00_plan/output/manifest-<slug>.md`.

## PROCESS
1. **Declared fetch (deterministic):** for each cross-tree `sources.declared[]` entry, copy → `output/<slug>/snapshot.md`, **unmodified**. `fetch(manifest) → snapshot`; same manifest → same snapshot.
2. **Exploratory discovery (judgment):** for each `sources.exploratory[]` entry, **search the named scope** (Grep / Glob / an Explore agent) for material matching the topic; identify the relevant files; copy them into the snapshot. This is where "explore an idea → search files → insight" happens. Use `cross-domain-map.md` to route to cross-domain scopes.
3. **Stamp provenance** → `output/<slug>/provenance.md` — every source pulled, declared *or* discovered; mark each `source-state` (settled/dormant | live).
4. **Extract (judgment):** pull **verbatim quotes + pointers** → `output/<slug>/signal-moments.md`. Never paraphrase; keep the snapshot reachable by `02_draft` for texture. **Tag authorship** on each pull — *the operator's own words* (usable as voice + texture) vs *retained AI output inside a source* (usable as substance only, **never** quoted as his voice — ROOT rule: raw assistant output is reasoning history, not synthesized voice). Authorship is a **separate axis from guard 6**: a source can be settled (guard-6 clean) yet AI-authored.
5. **Surface candidate angles:** from the signal moments, lay out the angle(s) the material actually supports — for the human to choose at the gate. Do **not** pick one unilaterally.

## OUTPUT
- `output/<slug>/snapshot.md` · `provenance.md` · `signal-moments.md` · `direction.md`

## GATE — the U-curve peak (discovered set → fidelity → ANGLE)
The *scope* was approved at the `00` gate; this gate reviews what discovery actually produced. Three checks:
1. **Discovered set + narrowing** — did the agent narrow the scope to the right place, and is the discovered source set right? This is where exploratory fan-in's **autonomous narrowing** gets human sign-off (the agent *proposes + discloses* the narrowing; the human approves). Snapshots are reversible, so reviewing post-fetch is fine — discard and re-search if the narrowing was wrong.
2. **Signal moments vs snapshot** — is the extraction faithful (incl. authorship tags); did the search miss anything?
3. **Set the angle** — the human chooses the angle from the surfaced candidates → `direction.md` (the chosen angle + which signal moments carry it). **The direction-setting decision — human, not the agent's.** Why this stage is the heaviest gate.

## SIX GUARDS (input fan-in done right)
1. **Conditional** — only when the post declares/needs external sources.
2. **One declared manifest** — the single throat; discovered sources land back in `provenance[]`.
3. **Fetch → local snapshot** — stages read the snapshot, never reach out live.
4. **One-directional, read-only** — never write back to a source project.
5. **Provenance-stamped** — what, from where, when.
6. **Stable / snapshotted sources** — a **live** source (e.g. another project's moving `CONTEXT.md`) is a **stop-and-reconsider** at the gate, not an input. If you need live material, the thinking hasn't settled — that's a reasoning signal.

## NOT
- Do not reach live into source projects once the snapshot exists.
- Do not summarize the snapshot away — the raw texture is the point.
- Do not let the agent decide the angle alone — surface candidates; the human sets direction at the gate.

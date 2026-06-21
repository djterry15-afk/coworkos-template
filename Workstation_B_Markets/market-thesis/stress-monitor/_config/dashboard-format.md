# Dashboard Format — _config (L3, stable across runs)
*The `03_render` output schema. The dashboard shows **readings + context**; it does not deliver a
verdict. The thesis call is the operator's, in the parent market-thesis project `CONTEXT.md`.*

---

## File: `03_render/output/<date>/dashboard.md`

## Sections

1. **Header** — run date · snapshot · one line: "readings + context, not a signal."
2. **Overall conditions** — the NFCI anchor: latest value, its plain-language description, where it
   sits in its own history (percentile, verbalized), GFC / COVID peaks, recent change.
3. **What the metrics say** *(the primary, legible layer)* — components grouped by role (e.g. funding
   plumbing / credit spreads). Each metric: latest value + units · a one-line `description` (from the
   manifest) of *what it is* · its position **verbalized** ("near the LOW / around the middle / near
   the HIGH end of its history") · recent change · GFC / COVID reference.
4. **Table (visual reference)** — the compact one-row-per-metric table (renders aligned in a markdown
   preview): `metric · latest (date) · 1w Δ · 1m Δ · %ile · GFC peak · COVID peak · dir`.
5. **Notes** — any series excluded (failed fetch) · any context window a metric's history can't cover.

*Plain-language descriptions live in `manifest.json` (`description` / `group`) — configure-once; the
renderer only formats them. B (HTML dashboard) and C (charts) are deferred to the widen phase.*

## Rules

- **Every number traces to the snapshot.** If it isn't in `02_transform/computed/<date>.json`
  (which derives only from the snapshot), it isn't in the dashboard.
- **No verdict, no signal, no alarm threshold.** Absolute thresholds don't transfer across episodes —
  so the dashboard reports *where readings sit*, and the human concludes.
- **State what's missing.** An excluded series or an uncoverable context window is shown explicitly,
  never hidden.

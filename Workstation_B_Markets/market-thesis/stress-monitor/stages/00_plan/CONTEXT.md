# 00_plan — Confirm the Standing Manifest (L2 stage contract)
*One job: confirm (or edit) the standing manifest before fetch. NO fetching here. A light gate.*

---

## What this is

The deterministic archetype has no per-run seed — the manifest is **standing config**. So this
stage is not "plan a run," it is "**confirm the factory is configured as you want**." On a
steady-state run it collapses to a yes. It does real work only when you add / change / drop a metric.

---

## Contract

| | |
|---|---|
| **Input** | the standing manifest (`_config/manifest.json` + `manifest.md` rationale) |
| **Skip** | FRED · the snapshot · downstream stages · the parent thesis `CONTEXT.md` |
| **Output** | an approved manifest (no new file on a steady-state run; an edited `manifest.json` if changed) |

---

## Process

1. Open `_config/manifest.md`. Are the metrics still the ones you want to monitor?
2. **If unchanged** → approve. Proceed to 01_fetch.
3. **If changing** → edit `_config/manifest.json` (the authoritative list), update the rationale in
   `manifest.md`. That edit *is* the configure-the-factory act — the one place judgment lives.
4. **First run only:** the series are candidates — confirm the 00-gate decisions in `manifest.md`
   (funding-spread choice, term-premium series, any add/drop).

---

## GATE (light) → 01_fetch

Approve the manifest before fetch. Adding/changing a metric is a logic decision — yours; do not let
the agent silently swap a series id.

---

## What NOT to do

- No fetching, no network here — that is 01's job.
- No interpreting readings — the manifest is about *what to monitor*, not *what the data says*.

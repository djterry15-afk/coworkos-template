# The Standing Manifest — rationale (L3)
*The authoritative list is `manifest.json` (machine-readable, read by the scripts). This file
explains **why these metrics** and records the 00-gate decisions. If the two ever disagree,
`manifest.json` wins — fix this doc.*

---

## The configure-once intelligence

This manifest is the entire intelligence-spend of the factory. Choosing *which* metrics monitor
market-stress plumbing is a judgment made **once** (and revisited rarely, at the 00 gate); the
scripts then run it forever. That is the deterministic archetype's defining move.

## Why these metrics (raw-primary + one composite anchor)

Per the decision (both, raw-primary), the dashboard leads with raw leading components at their real
units, with **one** official composite as a glance-level context anchor. Grounded in an upstream research
finding (the kind the research-factory archetype produces): the **funding-plumbing** metrics *lead*;
credit spreads *lag / confirm*; and absolute thresholds don't transfer across episodes — so the dashboard
shows **readings + historical context**, never a fixed alarm level.

| Metric | FRED series | Role | Why |
|---|---|---|---|
| **NFCI** (anchor) | `NFCI` | composite context | one-number "are conditions tight overall"; *their* weighting, taken as-is |
| **10Y term premium** | `THREEFYTP10` | leading (context) | compensation for duration risk; a leading plumbing gauge |
| **SOFR − EFFR** | `SOFR`,`EFFR` | leading (funding) | secured-vs-unsecured funding divergence; repo-stress proxy |
| **HY credit OAS** | `BAMLH0A0HYM2` | confirming | high-yield risk premium; the lagging/confirming signal |
| **IG credit OAS** | `BAMLC0A0CM` | confirming | investment-grade risk premium |

## 00-GATE — these are CANDIDATES until approved (first run)

The exact series are **candidates** pending the first 00-gate sign-off (per the build spec: series
selection is a gated build step, not a pre-build decision). Decisions to confirm at the gate:

- **Funding spread choice.** Candidate = `SOFR − EFFR` (both exist from 2018, covers COVID). Note:
  a `SOFR − IORB` spread is the cleaner repo-vs-admin-floor gauge **but `IORB` only starts 2021-07**
  (it replaced IOER), so it misses COVID. Pre-2018 episodes (GFC, the 2019 repo spike) have **no
  SOFR at all** — funding-stress history is structurally short. Confirm the choice.
- **Term-premium series.** Candidate = `THREEFYTP10` (Kim-Wright). Alternative: NY Fed ACM
  (`ACMTP10`) if preferred / available on FRED.
- **Add/drop** any component.

History note (watch-item): series start dates are **uneven** — `THREEFYTP10`/`NFCI`/credit OAS reach
back to/through the GFC; SOFR-based spreads do not. The transform falls back to *max-available
history* per metric and labels context windows it cannot cover.

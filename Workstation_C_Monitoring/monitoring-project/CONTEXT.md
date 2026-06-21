# CONTEXT.md
*Project: monitoring-project — the live synthesis (L1-as-synthesis at the project tier).*

> **STOP:** read this project's `CLAUDE.md` before this file.

---

## CURRENT STATE

*(Placeholder — your real synthesis lives here.)* What the monitor watches and why this metric set: the
standing rationale behind `stress-monitor/_config/manifest.json`. Any conclusion you draw from the readings
lands here (or upstream), dated and additive — not in the pipeline.

## THE TIER-4 FACTORY

`stress-monitor/` is the production workflow beneath this project — the **deterministic / monitor**
archetype. It pulls a standing set of public FRED financial-stress series → computes readings + historical
context → renders a dated markdown dashboard, with two light gates (confirm the manifest at `00`, glance the
dashboard at `03`) and no hard gate. It is **runnable out of the box** with your own free FRED API key (see
`stress-monitor/.env.example`). The example metric set (financial-stress plumbing) is illustrative — swap
in whatever recurring data stream you actually monitor. See `stress-monitor/CLAUDE.md`.

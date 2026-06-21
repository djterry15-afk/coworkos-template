# manifest — sample-stress-metrics-lead-lag
*ILLUSTRATIVE sample run. Shows the four-stage shape end-to-end; the sources are placeholders, not real
citations. Replace with a real seed + real sources when you use the factory.*

```
seed:
  question: "When financial stress hits, which market metrics move *first*, and which only
             confirm the move after it is already underway?"
  slug:     sample-stress-metrics-lead-lag
  scope:    external-only          # default; no workspace fan-in

declared[]:
  - (none — sources are discovered in 01_source)

reliability-bar: A/B only as evidence; C-grade and AI-authored → leads, never cited.
```

*The angle is not pre-decided. It is set at the `01_source` gate after the candidate ledger is approved —
see `sources-...md`, then `brief-...md`.*

*Composition note: this brief's finding is exactly what the **sibling `../../stress-monitor/`** monitors —
the **acquire → monitor seam**. Research establishes *which* metrics lead; the monitor then watches them
every run. And once accepted, the brief's sources are ingested into `../../llm-wiki/` (the *organize* step).*

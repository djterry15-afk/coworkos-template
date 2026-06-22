# Funding-Plumbing Metrics Lead Credit Spreads — Session Distillation
*(Example.) 2026-06-21. A spent-reasoning record: the session that set the lead/lag call. Digested — the
conclusion already lives in the project `CONTEXT.md`; this file is the trace behind it, kept so the verdict
can be audited back to its source.*

---

## Question
Which stress metrics give the earliest warning of funding strain — credit spreads, or the funding-plumbing
series?

## What was reasoned
The `research-factory/` produced a graded brief
([sample](../research-factory/_archive/sample-stress-metrics-lead-lag/brief-sample-stress-metrics-lead-lag.md))
weighing four independent sources on lead/lag behaviour across past stress episodes. Credit spreads (OAS)
**lag** — they widen *after* funding strain is already visible in the plumbing. The funding-plumbing series
(repo/SOFR spread, a financial-conditions index) **lead**. The organized detail behind each source lives in
the wiki ([financial-stress-indicators](../llm-wiki/wiki/financial-stress-indicators.md)).

## Conclusion (flushed to CONTEXT.md)
The verdict treats the **funding-plumbing** metrics as the early-warning set; credit spreads are
*confirmation*, not trigger. This is the rationale for the `stress-monitor/` manifest — those are the series
it watches on a schedule.

## Trace
- Evidence (graded): `research-factory/_archive/sample-stress-metrics-lead-lag/`
- Organized sources: `llm-wiki/wiki/financial-stress-indicators.md`
- Encoded as monitoring: `stress-monitor/_config/manifest.json`
- Governed by: `references/verdict-change-rule.md` (the standing rule this conclusion obeys)

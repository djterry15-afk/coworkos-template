# CONTEXT.md — 02_test (Layer-2 stage contract)
*A stage dispatcher in the pipeline-ICM body — the deterministic verification joint.*
*(Example stage — the link-checker build.)*

---

## What this is
Verify the artifact against fixtures: a folder of markdown with *planted* broken and valid links, whose
expected results are known. Pure determinism — the tests are scripts; no judgment in the middle. This is the
"scripts do the repetition" joint.

## Inputs
- The artifact from `01_build`.
- `fixtures/` — sample markdown with known broken + valid links.

## Process
1. Run `linkcheck` against the fixtures.
2. Assert it flags every planted broken link and passes every valid one (**no false positives**).
3. On failure the run stops here — fix in `01_build`; don't wave it through.

## Outputs
- `output/test-report.md` — pass/fail per fixture.

## GATE — on the results
Green tests are the bar to reach `03_release`. A red test blocks release — it is not a judgment call.

## What NOT to do
- Don't edit the artifact here — failures route back to `01_build`.

# 02_extract — Snapshot → Evidence (L2 stage contract)
*One job: **curate** the raw snapshots into a structured evidence file — pull what the graded sources
actually say, verbatim. Constrained execution — the lightest gate. (The snapshot is a full/raw capture;
this is where selection happens, and the fidelity gate checks the pulled items against that raw source.)*

---

## Contract

| | |
|---|---|
| **Input** | `01_source/<slug>/` snapshots + `sources-<slug>.md` |
| **Also load** | — (grading is done; work from the snapshot) |
| **Skip** | the web (no re-fetching) · the wiki · _config craft already applied |
| **Output** | `02_extract/evidence-<slug>.md` |

---

## Process

1. For each **A/B** source, pull the claims/data that bear on the question — **verbatim** quotes
   or exact figures, each with a provenance pointer into the snapshot.
2. Tag each extracted item **FOR / AGAINST / mixed**, relative to the question.
3. Carry the source's grade + authorship tag onto each item.
4. Leave **C-grade / ai-authored** out of the evidence (note as a lead only if it led somewhere).

---

## GATE → 03_synthesize

the operator confirms the extracted evidence **faithfully matches the snapshot** — no drift, no
paraphrase passed off as a quote. An item that can't be traced to the snapshot is removed.

---

## What NOT to do

- No new sourcing. If a gap appears, that is a **re-run of 01**, not a quiet web search here.
- No synthesis or verdict yet — extract what sources *say*; don't weigh them.

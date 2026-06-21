# 01_source — Find & Grade the Evidence (L2 stage contract)
*The acquisition stage and the **U-curve peak.** Split by the gate: discover + grade + propose a
candidate ledger (pre-gate) → human approves → commit full snapshots of approved sources only (post-gate).*
*The durable snapshot **follows** approval, not precedes it.*

---

## Contract

| | |
|---|---|
| **Input** | `00_plan/manifest-<slug>.md` |
| **Also load** | `_config/reliability-bar.md` · `_config/provenance-rules.md` · `../llm-wiki/wiki/index.md` (precheck) |
| **Skip** | **`../CONTEXT.md` (the thesis synthesis)** · downstream stage contracts |
| **Output** | (pre-gate) `01_source/<slug>/sources-<slug>.md` candidate ledger → (post-gate) `01_source/<slug>/snapshot-*.md` full captures |
| **Skills** | **Web Search** — *when* discovering sources · **WebFetch→save** — *when* the source is a discrete public page/PDF (the common case) · **web-capture** (browser) — *when* the page is gated / JS-heavy / blocks WebFetch (e.g. a 403) |

---

## PRE-GATE — discover → grade → propose

1. **Wiki precheck (consult, NOT fan-in).** Query `../llm-wiki/` via its index for what's already held;
   read the relevant pages. Target the *gap*; do **not** re-snapshot wiki-held material — cite it as
   already-held. *(this is often where the highest-value finding comes from — it can expose that the
   wiki's "corroboration" is a single institution.)*
2. **Discover.** Read declared sources (manifest) + web-search the gap (exploratory; workspace only if
   scope = `+workspace`). Fetch-to-**read** for assessment — transient, **not** yet a committed snapshot.
3. **Grade** every candidate (A/B/C + authorship + state + how-found) per `reliability-bar.md`.
4. Write the **candidate ledger** `sources-<slug>.md`: discovered sources · proposed grades · provenance
   metadata · leads held back. **No committed snapshots yet.**
5. **Surface the angle** the evidence points to — a *candidate for the operator*, not a decision.

## GATE (U-curve peak — mid-stage)
the operator approves, in order: **(a)** the candidate **source set** — right sources, nothing missing, scope
honoured; **(b)** the **grades** + authorship; **(c)** the candidate **angle**. **Disclose any narrowing
you did.** Weak / AI-authored sources demoted here.

## POST-GATE — commit snapshots → 02_extract
6. Snapshot **only the approved sources**, **full/raw** (the whole relevant source text, not a pre-curated
   few lines — curation is 02's job), each with the provenance stamp; pick the capture tool per the Skills
   row. **Failed capture (403 / paywall / JS) → exclude the source and re-grade without it; never
   paraphrase a search-result summary in place of a snapshot.** Mark in the ledger which approved sources
   captured vs failed.

---

## What NOT to do
- Don't re-snapshot wiki-held material — consult it, don't re-acquire it.
- Don't narrow scope on your own. Don't cite C-grade or ai-authored material as evidence.
- Don't commit snapshots before the gate. Don't pre-curate the snapshot — capture raw, curate at 02.
- Don't load the thesis synthesis (`../CONTEXT.md`). Self-contained.

# ICM — Interpretable Context Methodology (distillation)
*What this is: a digest, in our own words, of the methodology this workspace implements — folder structure as
agent architecture. When to use it: read it for the theory behind the tier tree and the stage pipelines.*
*Source: Jake Van Clief & David McDermott, "Interpretable Context Methodology: Folder Structure as Agent
Architecture," arXiv:2603.16021 (the protocol is MIT-licensed). This file is a summary, not the paper.*

---

## The core argument
Multi-agent frameworks (LangChain, AutoGen, CrewAI) suit complex, concurrent systems. But for **sequential
workflows where a human reviews each step**, they add engineering overhead the problem doesn't require. ICM
replaces that overhead with a folder: the filesystem *is* the architecture. One agent reads different context
at each stage, instead of many agents coordinating through code.

## The control surface — why it matters
| Want to do | Framework | ICM |
|---|---|---|
| Change stage order | Edit orchestration code, redeploy | Rename / reorder folders |
| Modify a prompt | Edit agent config in code | Edit a markdown file |
| Add / remove a stage | Write a new agent class | Add or delete a folder |
| Inspect what happened | Add logging, build a dashboard | Open the folder, read the files |
| Hand off to someone | Document env + dependencies | Copy the folder |
| Who can change it | A developer | Anyone with a text editor |

The cost ICM accepts: no automated error recovery, no concurrent execution, no AI-driven mid-pipeline
branching. Real limits — and irrelevant for sequential, human-reviewed work.

## The five principles
- **One stage, one job.** Each stage does a single step and writes to its own folder.
- **Plain text as the interface.** Stages talk through markdown/JSON; any tool or human can read and edit any artifact.
- **Layered context loading.** Load only what the current stage needs — less irrelevant context, better output. Prevents bloat rather than compressing it away after the fact.
- **Every output is an edit surface.** A stage's output is a file a human can open, edit, and save before the next stage runs.
- **Configure the factory, not the product.** Set the workspace up once (preferences, structure); each run reuses that config to make a new deliverable.

## The five layers (a layer is a job a file does)
```
L0  CLAUDE.md          "where am I?"              (map)
L1  CONTEXT.md         "where do I go?"           (route / synthesis)
L2  stage CONTEXT.md   "what do I do?"            (stage contract)
L3  reference          "what rules apply?"        (stable, internalized)
L4  working artifacts  "what am I working with?"  (per-run input/output)
```
L0–L2 route; L3–L4 carry content. **A layer is a job, not a tier** — this template stacks these layers across a
tier tree (ROOT → WORKSTATION → PROJECT → WORKFLOW); the tier-1-2 and tier-4 models show how they map.

## L3 vs L4 — the distinction that does the work
Reference (L3) is the *recipe* — stable across runs, internalized as constraints (voice, conventions). Working
(L4) is the *ingredients* — changes every run, processed as input (research, drafts). Mixing them in one
context forces the model to sort them; separating them by folder hands it already-organized context.

## Stage contracts
Each stage's `CONTEXT.md` spells out **Inputs / Process / Outputs**. The Inputs table is the control point:
without it the agent loads everything or guesses; with it, context selection is explicit, editable, auditable.

## Where ICM fits — and doesn't
Fits: sequential workflows, human review adds value at each step, the same pipeline reruns with new input,
non-developers need to adjust it. Doesn't: real-time multi-agent loops, high-concurrency multi-user systems,
AI-driven branching mid-pipeline.

## One discipline to keep: edit source, not output
When a stage output is wrong you can patch the output (fixes this run) or trace to the source file that
produced it (fixes every future run). Recurring edits in the same spot are a signal the stage contract or a
reference file has a fixable gap. Patch creative one-offs; fix the source for recurring patterns.

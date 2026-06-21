# manifest-schema.md — the ICM Inputs table, keyed by post
*The one declared throat for a run's inputs (guard 2). Explicit, editable, auditable. Built during `00_plan`, completed by `01_collect`. **No pre-decided angle** — the angle is set at the `01` gate.*

---

## SCHEMA

```
seed:                                   # the run's input — ONE post idea (a TOPIC, not an angle)
  from:            <entry-prompt | tier-3 idea-backlog path | campaign batch>
  topic:           <one line — what this post explores>
  platform-intent: [linkedin, ...]      # light call — which platforms this MIGHT suit.
                                         # NOT a locked set; refined on demand at 03_adapt.

post:
  slug:        <kebab-case-id>
  backlog-ref: <arc beat | one-off>     # if pulled from the Skeleton / a campaign; else one-off

sources:
  declared[]:                           # KNOWN sources, named at plan time
    path:        <repo-relative path>
    grade:       <A | B>                # A = backlog/recipe-mapped; B = off-arc, hand-supplied
    location:    <same-tree | cross-tree>   # cross-tree = outside the parent content project → always fetched
    why:         <what this source carries for THIS post>
  exploratory[]:                        # WHERE to look — discovery happens in 01_collect
    scope:       <folder / project to search>
    looking-for: <what kind of material, relative to the topic>
    # 01_collect searches the scope, then records what it found in provenance[]

provenance[]:                           # filled by 01_collect — one row per source actually pulled
  source:       <path>
  fetched-to:   <snapshot path>
  fetched-when: <date>
  source-state: <settled/dormant | live>   # guard 6 — a LIVE source is a stop-and-reconsider, not an input
```

## NO ANGLE HERE
The manifest **scopes the run** (topic + where to look). It does **not** carry the angle. The angle is discovered from the pulled material and **set by the human at the `01_collect` gate** (the U-curve peak), recorded in `01_collect/output/<slug>/direction.md`. `00_plan` plans the run; it does not decide what the post argues.

## THE TWO AXES (keep them separate)
- **`grade` governs manifest *weight*.** Grade A: cite the backlog/recipe row, light declaration. Grade B: hand-supply path + full `why`.
- **`location` governs *fetch*.** cross-tree → always fetch to a local snapshot with provenance (guards 3 + 5), regardless of grade. same-tree config already lives in `_config/` and isn't re-fetched. (Grade ⊥ location — a source can be Grade-A *and* cross-tree, so fetched.)

## TWO MODES OF FAN-IN
- **Declared** (`sources.declared[]`) — you already know the file; `01` fetches it deterministically (`fetch(manifest) → snapshot`).
- **Exploratory** (`sources.exploratory[]`) — you know the *topic* but not the file; `01` searches the named scope to **discover** sources, then snapshots them. The dominant case (explore an idea → search files → insight). Discovery is judgment (the research joint); everything found still lands in `provenance[]`, so the one-throat guard holds.

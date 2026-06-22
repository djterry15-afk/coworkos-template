# Naming Conventions
*What this is: the file/folder naming rules the workspace obeys, as a quick-reference card. When to use it:
at create time, so a new folder or file sorts and loads correctly. When to skip: never needed mid-reasoning —
pull it only when making something.*
*(ILLUSTRATIVE example entry — replace with your own reference material.)*

---

- **`_reasoning-log/`** — leading underscore = out of the primary load path (spent thinking). Not `_archive/`
  (too generic — this is specifically reasoning history).
- **`index.md`** — the control point inside any collection (`library/`, `_reasoning-log/`, a wiki's `wiki/`).
  One line per item; read it first, load selectively.
- **`CLAUDE.md` / `CONTEXT.md`** — the two primitives at every tier. `CLAUDE.md` = map + routing (L0/L1);
  `CONTEXT.md` = synthesis, or the operator contract at ROOT (L1).
- **lowercase-with-hyphens** for content files, named for the topic (`prompt-patterns.md`) — not the date.
- **`00_`, `01_`… numeric prefixes** — only inside a tier-4 `stages/` pipeline, where the number is
  execution order. Don't number reasoning-tier folders.
- **No empty folders** — create a folder when its content earns it (*state gates structure*). Until then,
  note the slot as *reserved* in `CLAUDE.md`.

---
name: distillation
description: Session close skill — produces a structured distillation of the current session. Extracts decisions, models, constraints, open questions, and CONTEXT.md updates.
trigger: Invoke when a session's reasoning clears the keep-it bar (see ROOT CONTEXT.md §Memory Protocol) — not automatically every session.
tier: ROOT
location: 00_Resources/references/skills/distillation.SKILL.md
---

# Session Distillation

## Instructions

Produce a structured distillation of this conversation as a context document.
Your job is extraction, not summarization. Pull only what's load-bearing —
decisions made, models built, constraints discovered, questions still open.
Leave the exploration, tangents, and repetition behind.

Output the following sections and nothing else:

---

# [Topic] — Session Distillation
*Date: [today's date] | Domain: [workstation / project]*

## 1. Key Decisions Made
Bullet list. Conclusions reached, directions chosen, things ruled out — with
brief reasoning where the reasoning matters. If a decision could drift or be
second-guessed later, capture why it was made, not just what it was.
If no decisions were made, write: "None — exploratory session."

## 2. Mental Models & Frameworks Developed
Bullet list. Ideas, reframings, or conceptual structures that actually moved
the thinking forward. Not every concept discussed — only what landed and
is worth carrying forward.
If none, omit this section.

## 3. Constraints & Gotchas Discovered
Bullet list. Things that are harder than they looked, failure modes identified,
design decisions that constrain future choices, or traps to avoid.
If none, omit this section.

## 4. Open Questions Remaining
Bullet list. Unresolved threads that belong in the next session or a future
decision point. Not wishlist items — only questions where the answer would
change what gets built or decided.
If none, write: "None — session fully resolved."

## 5. CONTEXT.md Updates
Surgical write actions only. One entry per update. No narrative.

**File:** [exact file path]
**Section:** [section name]
**Action:** ADD / CHANGE / REMOVE
**Entry:**
[exact text]

Repeat the block above for each update. If no CONTEXT.md files need
updating, write: "None — no context changes this session."

*If your memory protocol permits direct writes, apply these CONTEXT.md updates
directly after producing this distillation.*

---

## Quality Check Before Outputting
- Is every bullet load-bearing? If it wouldn't change anything to omit it, omit it.
- Are decisions captured with their reasoning, not just their conclusion?
- Is anything duplicated across sections? Remove the duplicate.
- Would a cold-start AI reading only this document know what was decided and why?
- Is every CONTEXT.md update surgical enough to paste directly? If not, tighten it.

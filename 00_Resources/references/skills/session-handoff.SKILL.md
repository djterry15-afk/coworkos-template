---
name: session-handoff
description: Creates a handoff document for the next AI session — operational context, not summary. Tells the next agent what to load, what happened at file level, what to do next, and what to avoid.
trigger: When work will continue in a new chat. Invoke with "create a handoff" or "write the handoff for next session."
tier: ROOT
location: 00_Resources/references/skills/session-handoff.SKILL.md
---

# Session Handoff Skill

## Purpose

A handoff is not a summary. A summary tells you what happened.
A handoff tells the next agent how to start.

The reader is a cold-start AI with no memory of this session. It has the
auto-loaded CLAUDE.md files and nothing else. Give it everything it needs
to pick up exactly where this session ended without asking a clarifying question.

---

## Instructions

Produce a handoff document and save it where it will be visible at session open.
Save at the tier where the work lives:
- ROOT-level or cross-workstation work → the workspace root
- Workstation work → the relevant workstation folder
- Project-specific work → the project folder

File name: `Next Session Handoff — [Topic].md`

Output the following sections in order. Every section is required.
Omit a section only if it genuinely has nothing — write "N/A" so it's clear
the omission was intentional, not an oversight.

---

## Output Template

```
# Next Session Handoff — [Topic]
*Created: [month year]. Consume at start of next session, then delete.*

---

## CONTEXT LOADING SEQUENCE

Load in this order before touching anything:

**Standard navigation (always)**
1. ROOT CLAUDE.md — auto-loaded
2. ROOT CONTEXT.md (operator contract + current state)
3. [Workstation]/CLAUDE.md
4. [Workstation]/CONTEXT.md

**Additional files — load before starting work**
[List any files beyond the standard sequence that the next agent needs.
Exact path. One line per file saying what's in it and why it matters for this work.
If a file was central to decisions made this session, list it here even if it's
not in the standard sequence.]

[Note which files were read this session but don't need re-reading next session,
and which should be re-read to verify current state before continuing.]

---

## WHAT THIS SESSION ESTABLISHED

[Factual log of what was done — at file level, past tense.
Not "we discussed X" — "X.md was rewritten to do Y" or "X was moved from A to B."
One bullet per meaningful change. Include exact paths.
If nothing was written/changed: say so and note what was decided instead.]

---

## ACTIVE STATE / CHANGE INVENTORY

[Where work stands right now.
If a task is complete: confirm it's done and what "done" means.
If mid-task: describe exactly where it stopped and what the next concrete step is.
If a multi-step change inventory exists (files to create, sections to move, etc.):
reproduce it here with the same level of specificity used this session —
what action, on what file, moving/creating what content, to what destination.
Include decisions made in conversation that aren't yet written in any file.]

---

## WORKING ORDER NEXT SESSION

[Numbered steps. Specific enough to follow without thinking.
If there's a dependency — do X before Y — make it explicit and say why.
If there are files to read before starting work, number those steps too.
Don't collapse multiple distinct actions into one step.]

---

## WHAT NOT TO DO

[Scope constraints: what's explicitly out of bounds this session.
Things that look relevant but aren't — and why they're excluded.
Decisions already made that shouldn't be re-opened.
Traps or failure modes identified this session.]
```

---

## Quality Check Before Saving

Read the output against each of these before saving:

- **Cold start test:** Can a fresh AI read only this document and start working
  without asking any clarifying questions? If not, add what's missing.

- **File-level specificity:** Does the context loading sequence give exact paths,
  not vague pointers ("load the workstation files")? Every file the next agent
  needs should be named explicitly.

- **No session memory assumed:** Does any section assume the next agent remembers
  this conversation? If yes, rewrite it as if starting from zero.

- **Active state is current:** Does ACTIVE STATE reflect the actual file state
  *after* this session's changes, not the state at the start?

- **Working order is followable:** Can you number the steps and hand them to
  someone who hasn't seen this conversation? If a step requires judgment the
  next agent won't have, add the context it needs inline.

- **Operational, not narrative:** Is anything phrased as summary ("we talked about X",
  "we agreed to Y")? Rewrite as instruction or fact ("X was decided because Y",
  "load X, then do Y").

- **Scope constraints are real:** Is WHAT NOT TO DO specific ("don't touch project-tier
  files — that's a separate session") or generic caution ("be careful")? Generic
  caution is noise. Remove it or make it specific.

# Build Protocol
*Trigger: End of any Session 1 (exploration) before handing off to Session 2 (execution).*
*Invoke with: "write the build spec."*

---

## How This Works

Every build moves through two sessions with a hard boundary between them.

**Session 1 — Explore**
Talk, reason, learn what's possible, discover constraints. Let it wander.
The AI helps you think. Nothing gets built.

**Session 1 Close — Write the Spec**
Use the extraction template below. The AI produces the spec from the session.
You review it. You approve it or send it back. Nothing proceeds without your sign-off.

**Session 2 — Execute**
Fresh conversation. The spec is the only input — no exploration history.
The AI asks clarifying questions about the spec, then builds exactly that.
If something unexpected surfaces mid-build, see "Mid-Build Rule" below.

---

## Operating Rules

**Before Session 2 starts:**
- The spec must be complete enough that a stranger could build from it.
- If you can't approve it, the problem is in the spec — fix it in Session 1, not Session 2.
- Incompleteness is visible here, not after hours of building.

**During Session 2:**
- No scope additions. If a new idea surfaces, write it down and queue it for the next cycle.
- No goal changes. If the goal shifts, the spec is wrong — stop, surface it, decide whether to finish or restart.
- The AI flags when it hits a gap in the spec. You answer the gap, do not expand scope.

**Mid-Build Rule:**
When the spec breaks — an assumption was wrong, a constraint wasn't captured, something changed — stop. Do not patch forward. Surface the break explicitly: what broke, why, what the decision is. Then either finish the build as-specced and queue the change, or restart Session 2 with an updated spec.

---

## Build Spec Template

*Produced by the AI at end of Session 1. Reviewed and approved by you (the operator) before Session 2.*

---

# [Project Name] — Build Spec
*Date: [today's date] | Session 1 topic: [one-line description]*

## 1. What Is Being Built
One sentence. Concrete noun, not a concept.
If you can't write this in one sentence, Session 1 is not done.

## 2. What Done Looks Like
Bullet list. Acceptance criteria only — observable outcomes, not implementation steps.
Each bullet should be answerable yes/no: does it do this or not?

## 3. Hard Constraints
Bullet list. Non-negotiables that limit how it gets built.
Technical limits, scope limits, things that cannot change.

## 4. Explicitly Out of Scope
Bullet list. Things that came up in exploration and were ruled out.
Naming them here prevents scope creep mid-build.

## 5. Assumptions Carried Forward
Bullet list. Conclusions from Session 1 that the executor needs to know.
Anything that was debated and settled. Reasoning matters here — not just the conclusion.

## 6. Open Questions (Spec Gaps)
Bullet list. Unresolved *design decisions that determine WHAT gets built* — folder
placement, schema, scope boundaries. A spec gap has an answer; it just hasn't been
decided. The test: **could you settle it at the whiteboard?** If yes, it's a spec gap.
**Gate: this list must be empty before Session 2.** An open spec gap means the spec is
not ready — resolve it in Session 1.

## 7. Acceptance Criteria & Watch-items (proving runs only)
*Skip this section for a known build. Use it when the build is a proving / first-of-kind
run whose point is partly to learn.*

Bullet list. *Empirical unknowns* that **cannot** be closed at the whiteboard because the
build itself is the experiment that resolves them. Name each as something to watch on the
run, with its mitigation if one exists. These do **not** block Session 2 — naming an
unknown as a watch-item is how a proving run passes the Section 6 gate honestly: a question
that can only be answered by building was never a spec gap. A break against one of these is
**data** — queue it as a finding (see Mid-Build Rule), do not patch it silently.

The boundary is the whole point: do not let a real spec gap hide here to dodge the gate
(an unmade decision is not an empirical unknown), and do not force an empirical unknown
into Section 6 where it would block a build that should proceed.

---

## Quality Check Before Approving

- Can a stranger read this and build the right thing without asking you questions?
- Is "What Done Looks Like" observable, not aspirational?
- Does "Out of Scope" capture everything that came up and was ruled out?
- Is the **Section 6 (Spec Gaps)** list empty? If not, go back. *(Section 7 watch-items
  may remain open — that is the proving-run exception, not a failure of the gate.)*

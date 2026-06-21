# Prompt Patterns
*What this is: reusable prompt structures for common agent tasks. When to use it: pull the matching pattern
when you're about to ask the agent to do one of these jobs, instead of re-improvising the framing.*
*(ILLUSTRATIVE example entry — replace with your own reference material.)*

---

## Extract-then-verify
> "Read <source>. Pull the N claims relevant to <question> as verbatim quotes with location pointers. Do not
> paraphrase. Then, separately, flag any claim you could not ground in the text."

Use when fidelity matters more than fluency — keeps extraction honest and separable from interpretation.

## Stress-test, don't agree
> "Here is my plan: <plan>. Before refining it, tell me the strongest reason it is wrong, and the one
> assumption it rests on that I haven't verified."

Use to get an opinionated review instead of agreement.

## Gate before write
> "Propose the change as a diff and wait. Do not apply it until I approve."

Use for anything that writes durable state — the human-gate pattern in prose form.

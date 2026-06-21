# core — sample-deleting-code
*ILLUSTRATIVE. The `02_draft` output: the platform-neutral core that executes the chosen angle. Craft is
edited here; the angle is not. The hub (`03_adapt`) renders this to each platform.*

---

I spent two hours this week refactoring one tangled function. By the end I had written almost nothing new —
I had mostly deleted.

The function was 300 lines. I pulled it into a handful of small ones, each doing a single boring thing. Net
change: about 180 fewer lines.

The surprise came halfway through. A bug I'd been chasing for a week just disappeared. It hadn't been fixed
— it had been *evicted*. It was living in a branch that no longer needed to exist once the pieces were
separate.

I keep relearning this. The progress wasn't the cleverness I added. It was that smaller pieces left the
problem nowhere to hide.

# linkedin — sample-deleting-code
*ILLUSTRATIVE. The `03_adapt` hub output: the core rendered to one platform sink (LinkedIn voice — insight
close). Adding a second platform later = re-run the hub with that platform's voice config; the core and the
angle don't change.*

---

I spent two hours refactoring one function this week and wrote almost no new code.

It was 300 lines doing five jobs at once. I pulled it into small functions, each doing one boring thing.
The file got ~180 lines shorter.

Then something I didn't expect: a bug I'd chased for a week was just gone. I hadn't fixed it. Splitting the
function had removed the branch it was hiding in.

The win wasn't the cleverness I added. It was the code I could finally delete — and how much a problem
shrinks when you leave it nowhere to hide.

---
*Status: publish-ready (not published). The factory halts at the hard gate before publish.*

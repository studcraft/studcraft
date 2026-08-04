# Design Process

**The questions to ask before adding a rule are the Design Checklist in
`CODE_OF_DESIGN.md`. There are seven. Ask them there, not here.**

This document used to open with five of them, reworded. The two it dropped
were *"Does it introduce unnecessary exceptions?"* and *"Does it reinforce
'Every Brick Matters'?"* — so anyone running the filter from this file was
running a checklist two criteria short of the constitution, without knowing
it. A "Preferred Design Patterns" list did the same thing to Principles 1, 4,
7, 11, 12 and 15, compressing each to a two-word bullet.

What follows is the part that is genuinely this document's own.

---

# Rule Hierarchy

The checklist tells you whether a rule belongs. This tells you **where to
reach first** when it does. When several solutions would work, prefer them in
this order:

1. Physical construction
2. Existing rules
3. New modular rule
4. New subsystem

New subsystems should be introduced only when absolutely necessary.

The ordering is the point, and it is the reason this section survives.
`CODE_OF_DESIGN.md` argues each level separately — Principle 3 for
construction over abstraction, Principle 15 for extending rather than
replacing, Principle 11 for the simpler of two solutions — but never ranks
them against one another. The ranking is what tells you what to try when more
than one would work.

---

# Decision Filter

Before submitting a proposal, re-run the Design Checklist in
`CODE_OF_DESIGN.md` against the finished text, not against the idea you
started with. A proposal drifts while it is being written, and the version
submitted is the one that has to pass.

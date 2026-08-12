# Design Process

**The questions to ask before adding a rule are the Design Checklist in
`CODE_OF_DESIGN.md`. There are seven. Ask them there, not here.**

---

# Rule Hierarchy

The checklist tells you whether a rule belongs. This tells you **where to reach
first** when it does. When several solutions would work, prefer them in this
order:

1. Physical construction
2. Existing rules
3. New modular rule
4. New subsystem

New subsystems only when unavoidable.

The ordering is why this section exists. `CODE_OF_DESIGN.md` argues each level
separately — Principle 3, Principle 15, Principle 11 — but never ranks them
against one another.

---

# Decision Filter

Before submitting, re-run the Design Checklist against the finished text, not
against the idea you started with. A proposal drifts while it is written, and
the submitted version is the one that has to pass.

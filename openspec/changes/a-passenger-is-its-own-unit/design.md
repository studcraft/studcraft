# Design — A passenger is its own unit

## Decision 1 — No `docs/NN-units.md`

A units document was considered on the analogy of `11-combat.md` and
`12-melee.md`. The analogy does not hold: melee is a **subsystem** — its own
contact requirement, its own striking ends, thirteen rules, and `MEL-012`
importing combat wholesale to declare its exceptions. "Unit" is a **term**, and a
document per term is a glossary with headings.

It would also cost more than it creates. `02-core-rules.md` already owns the
taxonomy in its `# Unit Types` chapter, so a units document would not add one —
it would **move `CORE-003`, `CORE-004` and `CORE-005` out of the document that
has them**, which `scripts/check_id_stability.py` reports as three renumberings
and a required check then refuses.

`system/design-process.md` puts a new subsystem on the last rung of the Rule
Hierarchy, reached only when the rungs above are exhausted. They are not: an
existing chapter and an existing glossary carry this.

## Decision 2 — No `CORE-017 — Unit` either

The obvious repair is a rule defining the term. Two things argue against it.

**Placement.** `scripts/lint_ruleset.py` requires rule IDs to increase strictly
within a document. The highest CORE number is `CORE-016`, so a new rule is
`CORE-017` and must sit physically **after** it — the root of the taxonomy below
`# Battlefield Representation` and forty lines below the three types it governs.

**It is not needed.** Once `# Unit Types` lists only unit types, `CORE-003` and
`CORE-004` enumerate the category and `CORE-006` states what it does — activates,
receives 3 Action Points. What is missing is a place for a reader to *look the
word up*, and that is a glossary's job rather than a rule's.

Folding the definition into `CORE-006` instead was also rejected: that rule was
made single-purpose deliberately (`action-points-have-one-owner`), and giving it
a second job to save a glossary entry trades a clean rule for nothing.

## Decision 3 — The glossary creates the category, and there is precedent

`Delivery Method` is defined by no rule. The glossary states it — "Line of Sight
+ Range for ranged weapons, or Physical Contact for melee" — and cites the rules
that instantiate it. `Unit` has the same shape: a name spanning `CORE-003` and
`CORE-004`, used by `CORE-006`.

`docs/14-glossary.md` is in append order, so the entry goes last. The entry also
states that a structure is not a unit: `CORE-005` is the member a reader would
otherwise still infer from the chapter's history, and one clause is cheaper than
leaving the negative to be worked out.

**It does not print the allotment.** `CORE-006` owns how many Action Points a
unit has — `action-points-have-one-owner` retired `FLOW-005` for saying it and
stripped the number from `FLOW-004`, `FLOW-012` and this file's own *Activation*
entry, so reinstating it here would undo the change that cleaned it.

**And both its citations use the comma form**, not the parenthesised one.
`lint_ruleset.CROSS_REF_RE` pairs a filename with the next `(ABC-000)` inside
eighty characters; a parenthesis holding several IDs never matches, so the scan
runs past it and pairs that filename with the *next* one's citation. Written
parenthesised, this entry made a required check report `02-core-rules.md
(TRN-021), which does not exist` — a rule that exists, blamed on the wrong
document. Reordering the two citations silenced that, but left `CORE-006`
unchecked. The comma form fixes both: no parentheses for the scan to reach, and
`COMMA_REF_RE` captures every ID of both citations, so the entry reads
core-first the way a reader wants and every rule it names is verified.

This is a latent defect in the linter, not only in one entry: **every multi-ID
citation in `docs/` is currently unchecked**, silently. `docs/14-glossary.md`
already holds several. Repairing the regex would newly check citations that have
never been checked, across every document, which is its own change with its own
failures to work through — not this one's.

## Decision 4 — `TRN-021` answers one question and knowingly leaves another

It states that a model inside a vehicle keeps its own Action Points. It does
**not** state whether a transport may move and its passenger then activate and
disembark at the new position.

That is a design decision about how the game plays, not a gap in wording, and
nobody has taken it. It is open in the shipped ruleset today and this change
leaves it exactly as open — `09-transport.md`'s Purpose promises "how units
embark, **travel** and disembark" and no rule states what travelling is. Deciding
it belongs with whoever has played a game; stating the Action Point half now is
what makes those games possible.

## Decision 5 — No spec delta, and why

`openspec/specs/action-economy/spec.md` exists, and its *Universal Action
Points* requirement is what `TRN-021` reaches: its scenario already says "any
unit (infantry, vehicle, walker, hovercraft, or future unit type)".

**That requirement and its scenarios stay true, word for word.** The capability
says every unit receives the same allotment however it is built; this change
adds no unit type, changes no allotment and creates no exception. What it settles
is which models the existing word "unit" was always reaching — a question about
`docs/`, not about the capability. A delta restating an unchanged requirement is
the noise `system/proposal-review.md` ("Delta vs. Direct Edit") allows a
doc-edit task to avoid, provided the reasoning is written down. This is it.

## Decision 6 — `TRN-021` settles half of `TRN-008`, deliberately

`TRN-008` says opening or closing an access point costs 1 Action Point and does
not say who spends it. Decision 7 below cites that silence as the thing an
earlier audit assumed its way past. `TRN-021`'s second paragraph answers half of
it: for a model the vehicle carries, its own points pay.

**Taken on purpose, and it is the reading the shipped text already requires.**
`FLOW-007`'s Example D — `Open Ramp / Disembark / Close Ramp` — is a sequence of
three actions "combined freely during an activation", and one activation belongs
to one unit. Under any other reading the example is not executable at all.

What stays open is the other half: whether a model *outside* a vehicle may open
its access point. Nothing here reaches it.

## Decision 7 — The non-`docs/` file this branch carries

`system/proposal-review.md` gains a section on sizing a finding.
`system/repository-strategy.md` ("Branch Naming") requires a ruleset branch to
name such a file and say why, so: this change **is** the correction, and the
section is what stops the next one being needed.

A `ruleset-auditor` run over `docs/` reported that nothing defines a unit, and
ranked it a blocker on the strength of an argument that read `FLOW-007`'s
Example D as evidence for one side of a question `TRN-008` leaves open. The gap
was real; its size was not. What it takes to repair is one heading level and two
sentences, and a defect repaired by one heading level is not a blocker whatever
the symptom looked like.

The section states **one** test — find the repair before writing the severity —
and points at the section below it for how to rank, rather than restating it.
That neighbour, added earlier the same day, is the same failure seen from the
evidence side rather than the severity side. Both belong to
`system/proposal-review.md` because both auditors already read it for the
reporting format.

Shipping it separately would mean two branches whose only relation is that one
is the worked example of the other.

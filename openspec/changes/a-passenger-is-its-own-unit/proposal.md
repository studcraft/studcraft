# A passenger is its own unit

## Why

`CORE-006` gives every unit its Action Points. `FLOW-002` activates units one at
a time. **No rule and no glossary entry says what a unit is**, and four rules
charge an Action Point to a model a vehicle carries without saying whose points
those are: `TRN-006` (disembarking), `TRN-008` (opening or closing the access
point it uses), `VEH-013` (a minifigure taking over as Pilot) and `DMG-018` (a
Wounded Pilot or crew member recovering). `TRN-005` charges for embarking and
does name its actor — "the unit must be adjacent to a functional access point" —
but that unit is standing outside, so it says nothing about the model already
aboard.

Both readings are playable and they are different games. If an embarked model is
its own unit, a transport carrying eight infantry gives its owner nine
activations. If it is not, `DMG-018`'s clause about a Pilot recovering cannot be
executed, because the Pilot has no Action Points to spend.

The term is not missing by accident. `02-core-rules.md` has a `# Unit Types`
chapter, and it holds three rules: `CORE-003` Infantry, `CORE-004` Vehicles and
`CORE-005` Structures. **A structure is not a unit** — `CORE-005` calls
structures "permanent battlefield elements" and its own text says "How a *unit*
crosses or occupies these constructions", distinguishing itself from one. The
one place in the ruleset that enumerates units enumerates a non-unit, so a
reader who goes there to infer the term is misled.

## What Changes

### `docs/02-core-rules.md`: `CORE-005` leaves `# Unit Types`

Its heading drops from `##` to `#`. **No text changes, the rule keeps its ID and
its document, and it stays where it is in the file** — it stops being a member of
a chapter it was never a member of in fact. `# Unit Types` then holds exactly the
two rules that are unit types.

### `docs/14-glossary.md`: a `Unit` entry

The category has no owning rule and does not need one: `CORE-003` and `CORE-004`
instantiate it and `CORE-006` uses it. This is the shape `Delivery Method`
already has in the same file — a name for something spanning two rules, created
by the glossary and citing the rules underneath it.

### `docs/09-transport.md`: `TRN-021 — An Embarked Model Is Its Own Unit`

States that a model a vehicle carries remains its own unit and spends its own
Action Points. That is the answer the four rules above assume and none of them
gives. It also settles who funds `TRN-008` for an embarked model —
`design.md`, Decision 6.

The document's Summary gains a tenth principle saying the same, because
principles 5 and 6 state what embarking and disembarking cost and a reader meets
the costs there.

## Non-Goals

- **Activation order between a transport and its cargo.** Whether a transport may
  move and its passenger then disembark at the new position is a design decision
  nobody has taken, and it is open today. `TRN-021` closes one of two questions
  and leaves the other exactly as it was. `design.md`, Decision 4.
- **A `CORE-017 — Unit` rule.** Rejected — `design.md`, Decision 2.
- **A `docs/NN-units.md` document.** Rejected — `design.md`, Decision 1.
- **Restating "a vehicle is a unit" in `08-vehicles.md`, or aligning `INF-001`'s
  title with its body.** `CORE-004` under a corrected `# Unit Types` already does
  the first, and the second is cosmetic.
- **Defining "adjacent".** Considered and dropped: a player puts the model beside
  the access point and continues.

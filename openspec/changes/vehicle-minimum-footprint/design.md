## Context

`CORE-004` has said "one or more Unit Bases" since before vehicles had movement, terrain or Pilot rules to interact with. Each of those arrived later, and together they make the one-Unit-Base case incoherent rather than merely weak.

The trigger was noticing that `VEH-004`'s `3 ×` multiplier applied to a single Unit Base gives exactly 12 studs — the same as infantry. That is a coincidence of two numbers chosen independently, and chasing it turned up the real problem: the Pilot has nowhere to sit.

## Decisions

### The floor is derived, not chosen

An arbitrary "vehicles must be at least 2 UB" would work mechanically and sit badly against everything else in this ruleset, where every limit is read from the model: axle height, knee height, hover assembly height, plate layers, muzzle size.

The floor here is not chosen. `VEH-013` requires a Pilot; `TRN-014` and `CMP-013` say crew occupy Unit Bases. One Unit Base of vehicle containing one Unit Base of Pilot leaves zero Unit Bases of vehicle. The minimum is whatever those two rules imply, and today that is two.

This also means the rule stays correct if its inputs change. If crew were ever redefined as occupying less than a full Unit Base, the floor would move on its own rather than needing an edit.

### Scoped to powered vehicles

`VEH-013` says "every powered vehicle", and the constraint is entirely a consequence of needing a Pilot. Writing the floor as applying to *all* vehicles would over-reach.

No unpowered vehicle exists in the ruleset — searched the whole of `docs/` for trailers, sleds and towed anything, and found none. But `VEH-012` enumerates locomotion types rather than declaring that list closed, and a towed or unpowered thing is an obvious future addition. Scoping now means that addition needs no exception carved out of this rule later.

### `CORE-004` and `VEH-001` both change, because both state it

The two rules independently say "one or more Unit Bases". Fixing one and leaving the other is how this repo has repeatedly ended up with rules that contradict each other from different documents.

`VEH-013` carries the *reasoning*, because that is where the constraint originates; the other two state the consequence and cite it. That keeps one source of truth rather than three copies of an argument.

`CMP-002` gets a single sentence rather than the full derivation. It is the construction-side rule — a builder reading it wants to know the consequence for what they are building, not the chain that produces it.

### The alternative considered: leave it and let consequence teach

This repo used exactly that reasoning for the flat hover build in `VEH-024` — a hover model built with its hull on the ground has a Terrain Threshold of 0 and is blocked by everything, and the rule says so rather than forbidding it.

That works there because the consequence is *visible*: the model plainly is not finished. A one-Unit-Base vehicle looks perfectly finished and is subtly worse than walking, which teaches nothing. And unlike the hover case, this is not a bad build of a legal thing — the footprint cannot physically contain what the rules require inside it.

## Risks / Trade-offs

- **It forbids a build some player might want.** A one-man pod or a small drone is a reasonable thing to imagine. The ruleset's answer today is that a 1 UB self-contained machine is *cargo* (`TRN-013` lists "Drone — 1 UB"), not a vehicle. If drones ever want to move under their own power, that is a new category with its own rules, not a vehicle shrunk below the size of its own crew.
- **Nothing enforces it mechanically.** No linter can measure a LEGO model. Like every construction standard in this ruleset, it relies on the builder and the table.
- **A very small margin at the new floor.** A 1 × 2 UB vehicle is 6 studs long and moves 18 against infantry's 12. That is a real margin but not a large one, which is correct — a motorbike should beat a running soldier, not lap them.

## Open Questions

None. Not applied — proposal only.

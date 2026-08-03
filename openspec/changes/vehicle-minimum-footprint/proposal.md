## Why

`CORE-004` and `VEH-001` both permit a vehicle occupying a single Unit Base. Two independent rules make that build impossible to justify, and one of them makes it incoherent.

### A one-Unit-Base vehicle is entirely filled by its own Pilot

`VEH-013` requires a Pilot on every powered vehicle. `TRN-014` and `CMP-013` state that crew members occupy their own Unit Bases, separate from cargo capacity.

A vehicle whose total footprint is one Unit Base therefore has one Unit Base of Pilot inside one Unit Base of vehicle. **There is no vehicle left** — it is a minifigure with a shell. The contradiction is not about balance; the footprint cannot hold what the rules require it to hold.

### And it is strictly worse than the infantry model it costs the same as

Both consume 1 UB of Deployment Area (`DEP-003`, `DEP-004`).

| | Infantry | 1 UB vehicle |
|---|---|---|
| Movement per Action Point | 12 studs | **12 studs** — `VEH-004`'s `3 ×` applied to a 4-stud longest axis |
| Maximum weapon Range | 24 studs | **24 studs** — Platform Length 4 either way (`WPN-004`, `WPN-005`) |
| Requires a Pilot | no | **yes** (`VEH-013`) |
| One-brick obstacle | free (`MOVE-009`) | blocked unless its axle reaches 3 plate layers (`VEH-022`) |
| Stairs | may climb (`MOVE-013`) | **never** (`VEH-027`) |
| Can be stranded | no | **yes** (`VEH-025`) |

It ties on the two things a vehicle exists to be better at, loses on three, and costs an extra minifigure. No player should build one, and the rules currently invite them to.

### The ruleset already has the right category for a one-Unit-Base machine

`TRN-013` lists **"Drone — 1 UB"** as *cargo*, not as a vehicle. A self-contained object of that size already has a home in the rules, and it is not the vehicle rules. `CORE-004` simply contradicts that boundary by saying "one or more".

## What Changes

- **`CORE-004`** — a powered vehicle occupies **two or more** Unit Bases, with the reason stated: one is consumed by the Pilot.
- **`VEH-001`** — the same correction, since it independently states "one or more".
- **`VEH-013`** — carries the derivation, because that is where the constraint originates: a powered vehicle needs room for its Pilot in addition to its machinery.
- **`CMP-002`** — one sentence pointing at the consequence, since it is the construction-side rule a builder reads.

## Impact

**A minimum, but a derived one.** The floor is not a balance number chosen to make small vehicles viable. It falls out of two rules that already exist: a Pilot is required, and a Pilot occupies one Unit Base. Had either been different, the floor would be different. That matters, because an arbitrary threshold would sit badly against Principle 1 and against every other limit in this ruleset being read from the model.

**Scoped to powered vehicles**, following `VEH-013`'s own wording. No unpowered vehicle exists in the ruleset today — a repo-wide search finds no trailer, sled or towed anything — but if one is ever added it will have no Pilot, and a 1 UB unpowered vehicle would then be perfectly coherent. Writing the rule as "powered" now means that future addition needs no exception carved into it.

**Nothing legal becomes illegal in practice.** Every vehicle named anywhere in the ruleset is already 2 UB or larger: Bike 1 × 2, Buggy 2 × 2, Jeep 2 × 3, Tank 2 × 5, Heavy Transport 3 × 8 (`VEH-001`). This change forbids a build the rules permitted and nobody should have made.

**No numeric value changes**, no rule is added, removed or renumbered. The smallest legal vehicle becomes the Bike, which `VEH-004` already gives 18 studs of movement against infantry's 12 — the margin a vehicle is supposed to have.

Not applied — proposal only.

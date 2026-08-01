## Why

A full audit of `docs/07-movement.md` found **twenty-one defects**: three contradictions, eleven omissions, two duplications, three structural problems, and two in the falling rules found on a second pass. Movement is the only core system never audited, and it shows — the document answers "how far" but almost never "at what cost", and its two movement axes are specified to different levels of precision.

The central defect is that the document contradicts itself about what a movement action even is.

`MOVE-004` states "Standard infantry movement: **12 studs forward**", which reads as a fixed distance. `MOVE-007`'s worked example then moves a unit "Forward 8 studs", which is only legal if 12 is a maximum. Both cannot be true. And 8 is not a multiple of 3, so that same example also violates the grid-alignment justification `MOVE-004` gives for the number 12.

Everything else follows from the same root cause: forward movement was specified loosely, side movement was specified tightly, and nobody reconciled them.

| Axis | Maximum | Granularity | AP cost |
|---|---|---|---|
| Forward (`MOVE-004`) | 12 studs, or is it fixed? | unstated | 1 AP ✅ |
| Sideways (`MOVE-005`) | **unstated — no cap exists** | multiples of 4 ✅ | **unstated** |
| Backward (`MOVE-006`) | "the same movement allowance" | unstated | **unstated** |

As written, a unit may sidestep an unlimited distance for an unknown number of Action Points.

## What Changes

### Contradictions (3)

1. **`MOVE-004` states a fixed distance; `MOVE-007` assumes a maximum.** Establish that 12 studs is a maximum, not a fixed distance.
2. **`MOVE-007`'s example is illegal under `MOVE-004`'s own justification.** "Forward 8 studs" is not a multiple of 3, the Unit Base depth that justification invokes. Correct it to 6 studs, and state that forward and backward movement move in multiples of 3 — mirroring side movement's multiples of 4, the base's width.
3. **`MOVE-011` lists three legal access points; `MOVE-014` recognises two.** Ramps are silently dropped. Add them to `MOVE-014`.

### Omissions (11)

4. **`MOVE-005` has no maximum** — side movement is currently unlimited. Cap it at 12 studs.
5. **`MOVE-005` has no AP cost.** Add 1 AP.
6. **`MOVE-006` uses "the same movement allowance"**, a term defined nowhere in the ruleset.
7. **`MOVE-006` states no limit or granularity.**
8. **`MOVE-006` states no AP cost.**
9. **`MOVE-003` measures "from the front edge"**, which is wrong for backward and sideways movement. Restate in terms of the direction of travel.
10. **`MOVE-004` never states its granularity**, leaving forward movement's step size undefined.
11. **No rule covers plate-built obstacle heights.** A 4-plate wall falls between `MOVE-009` (1 brick) and `MOVE-010` (2 bricks) and is unresolvable. Express thresholds in plate layers, matching `16-damage-system.md` (DMG-003).
12. **`MOVE-010` never says whether climbing consumes the movement action** or is paid on top of it.
13. **`MOVE-012` / `MOVE-013` state no traversal cost.** The reader knows a 2-brick obstacle costs +1 AP but not what a five-brick staircase costs.
14. **`MOVE-015` never says whether a unit may fall deliberately, nor where it lands.**

### Duplications (2)

15. **`MOVE-003`'s "Models may not overlap" duplicates the Collision section.** Collision owns it.
16. **Doors, Ramps and Interactive Terrain each restate CORE-007's 1 AP cost.** Keep the movement-specific content — a closed door blocks movement, a lowered ramp becomes terrain — and let the cost live in CORE-007 alone.

### Structural (3)

17. **Collision, Doors, Ramps and Interactive Terrain carry normative rules with no rule ID**, so nothing can cite them. `08-vehicles.md` already cites `MOVE-008` by ID; there is no equivalent handle for "enemy units block movement". Promote them to `MOVE-017` … `MOVE-020`. No existing ID is renumbered.
18. **The Summary omits every AP cost** and restates the ambiguous "Infantry move 12 studs".
19. **`MOVE-016` cites its own document by filename** (`` `07-movement.md`, Vehicle Movement ``). Replace with a plain section reference.

### Falling (2)

Found on a second pass, after the rest of the audit was written. Both are in `MOVE-016`, which the first pass wrongly treated as already sound because a previous change had recently touched it.

20. **`MOVE-016` measures fall height in whole bricks**, so it would be the last place in the document still using that unit once defects 11's plate-layer conversion lands. A fall of 4 plate layers has no defined dice count, exactly the gap being closed for obstacles. Left unfixed, this change would *create* an internal inconsistency rather than remove one.
21. **A one-brick drop is a coin flip on being wounded, while a one-brick obstacle is free to cross.** `MOVE-009` treats 3 plate layers as trivial terrain; `MOVE-015` plus `MOVE-016` treat stepping off the same height as a 50% chance of a wound (one die, keep lowest, 1–3 fails). Nothing reconciles them. Add a minimum fall height below which no damage is rolled, set at the same 3 plate layers `MOVE-009` already calls trivial.

## Impact

**Two mechanical changes, stated plainly.**

*Movement.* Forward and backward movement become multiples of 3 studs, capped at 12, and side movement gains a 12-stud cap and a 1 AP cost. Previously forward granularity was undefined and side movement was uncapped and free. This tightens rather than loosens: no unit can do more than before, and the uncapped sidestep — almost certainly an oversight rather than a design choice — is closed.

*Falling.* A fall of 3 plate layers or less now causes no damage, where previously it forced a roll with a 50% chance of a wound. This one loosens, and it is the only change here that does. It is included because the alternative is a rule that contradicts `MOVE-009`: the same one-brick height is simultaneously trivial to climb over and dangerous to step down from. Dice are also now rolled per complete brick rather than per brick with no remainder rule, so a fall of 7 plate layers has a defined answer (2 dice) where before it had none.

The falling defects were found on a second pass, after the rest of the audit was written and after this proposal was first opened. `MOVE-016` had been skipped on the first pass because a recent change had touched it — which turned out to be exactly the wrong reason to skip a rule, since that change addressed the damage system's needs and never audited the rule on its own terms.

**Four new rule IDs** (`MOVE-017` … `MOVE-020`) for text that already exists and is already normative. No rule is renumbered, and no rule is deleted.

**No spec delta.** `openspec/specs/` has no `movement` capability; the four that exist cover damage and weapons. Creating one properly means capturing all twenty MOVE rules, not just the ones this change touches, which is its own piece of work. Recorded as follow-up rather than half-done here.

**Known asymmetry left open.** Quantising infantry movement to the Unit Base's own dimensions raises the question for vehicles, whose movement is `1.5 × length` (`08-vehicles.md`, VEH-004) and continuous. Infantry will move on a grid while vehicles do not. That is arguably correct — a vehicle's length is not a multiple of anything — but it is a real inconsistency and is deliberately out of scope here, since fixing it means reopening `08-vehicles.md`. Flagged for a future vehicle-movement audit rather than resolved silently.

Not applied — proposal only.

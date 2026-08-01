## Context

`VEH-004`'s `1.5×` and `WPN-005`'s `× 2` were both set before the rest of the numbers existed to check them against. `MOVE-004`'s 12-stud infantry move, `WPN-004`'s Platform Length cap and `CORE-001`'s Unit Base orientation all arrived later. Measured against those, both multipliers fail.

The failures are not equally serious. The vehicle one produces an oddity — a motorbike slower than a soldier — and an unmeasurable fraction. The weapon one disables ranged combat: with a maximum infantry Range of 8 against a 12-stud move, no unit can be engaged before it closes.

## Decisions

### `× 6` for Range, chosen from what makes ranged combat function

The requirement is that an attacker gets a meaningful window as an enemy closes. Infantry move 12 studs per Action Point and hold 3 AP, so 36 studs per turn.

| Multiplier | Infantry rifle Range | Action Points to close from max range |
|---:|---:|---:|
| × 2 (current) | 8 | 0 — already inside one move |
| × 4 | 16 | 2 |
| **× 6** | **24** | **2, with a full move of exposure** |
| × 9 | 36 | 3 |

`× 4` technically works but leaves 16 against a 12-stud move: the closing unit is exposed for a third of a move. `× 6` puts maximum range at exactly two infantry moves, so an approach costs two Action Points and takes fire on the way in. `× 9` makes a rifle reach a full turn of movement, which removes the approach decision entirely.

`× 6` is also the largest of these that keeps the mnemonic intact, being exactly twice the vehicle multiplier.

### `3×` for movement, chosen from the smallest vehicle

`2×` was considered first and rejected on one number: a Bike would move 12, exactly matching infantry, while costing twice the Deployment Area. A vehicle that ties a pedestrian and costs more is not a choice a player makes.

`3×` puts the Bike at 18 and every other vehicle proportionally above it. It also has a reading `1.5×` never had: **every vehicle covers three of its own lengths per action**, whatever its size. The Bike is not slow because it is small; it is simply small.

`4×` and beyond were not pursued. A Heavy Transport at 3× already moves 72 studs per Action Point, and the mnemonic relationship with Range would be lost.

### Both multipliers are whole numbers, and that is a requirement rather than a convenience

`1.5 × 9 = 13.5`. There is no half stud on a LEGO baseplate, and `07-movement.md`'s Design Philosophy explicitly asks for movement that is "easy to measure" and "free from templates and measuring sticks". Any multiplier that can produce a fraction fails that on its own, regardless of whether the resulting distance is well balanced.

This ruled out every non-integer candidate before balance was considered.

### No cap on Range, and the reasoning is borrowed rather than invented

The obvious objection to `× 6` is that a Tank reaches 90 studs and nothing stops a larger platform reaching further.

`WPN-021` already faced exactly this, for Impact Strength, derived from the same Weapon Length, in the adjacent rule — and refused to cap it, on the grounds that the limit is what the attacker's platform can carry. Capping Range would contradict that decision from one rule away, and would be the kind of local exception this ruleset has spent several changes removing.

The stronger argument is that the cap already exists and is simply not written as a number. `WPN-004` bounds Weapon Length by Platform Length; `SCS-003` and `DEP-003` bound platform size by the agreed Deployment Area; `FLOW-001` requires the battlefield to be agreed before the deployment size. Each link is either read from the model or negotiated, which is how every other quantity in this game is bounded.

The arithmetic confirms it rather than merely asserting it: the 3 × 10 UB super-heavy that would reach 180 studs consumes 30 UB of Deployment Area and cannot be fielded in a Skirmish (25 UB) at all.

What is added is a paragraph stating this inside `WPN-005`, in the same shape `WPN-021` uses for its own missing cap. A reader who computes 90 studs and worries should find the answer where they are already reading.

### Line of sight is named as the practical limit, because it is easy to miss

`CORE-008` uses true physical visibility, so a 90-stud Range only matters where 90 studs of clear sight exist. That bound is real and already in the rules, but it lives in a different document, and nothing in `WPN-005` points at it. One sentence fixes that.

The movement equivalent is worth stating for the same reason: a 24-stud transport moving 72 studs needs a clear lane of nearly a hundred, which terrain rarely offers.

### Infantry movement is deliberately untouched

`MOVE-004`'s 12 studs is the reference every figure above was judged against. Changing it would move the target while measuring, and nothing found here suggests it is wrong — a rifle at two moves and a bike at 1.5 moves both read correctly against it.

## Risks / Trade-offs

- **This changes every distance in the game.** Unlike the recent audit work it will be felt at the table immediately, and it deserves playtesting attention in a way documentation fixes did not.
- **Tank ranges look extreme on paper.** 90 studs is roughly 72 cm. On an open table a large gun will dominate, which is intended; the counter is terrain, and terrain is player-built. If playtesting shows it dominating even on dense tables, the lever is the multiplier, not a cap.
- **A Heavy Transport at 72 studs per Action Point is a large number.** It is self-limiting in practice — a vehicle that long rarely has a clear lane of 96 studs — but it is the figure most likely to look wrong in isolation.
- **The mnemonic ties the two multipliers together.** "Move three, shoot six" is memorable precisely because the numbers relate, which means changing one later without the other loses that. Worth accepting: the relationship is the reason both numbers are easy to hold.

## Open Questions

None. Not applied — proposal only.

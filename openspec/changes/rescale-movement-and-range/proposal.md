## Why

Two multipliers were set before there were enough other numbers to check them against. Measured now, both are wrong, and one of them quietly disables a whole subsystem.

### Ranged combat barely functions

| | |
|---|---|
| Longest weapon an infantry model may carry (`WPN-004`, Platform Length 4) | 4 studs |
| Its Range at `Weapon Length × 2` | **8 studs** |
| Infantry movement per Action Point (`MOVE-004`) | **12 studs** |

**A unit closes faster than it can be shot at.** Anything standing at the edge of your maximum range reaches physical contact in a single Action Point, having taken no fire at all. The muzzle-counting, Attack Dice, Impact Strength and Geometry Check machinery exists for a subsystem that a player has almost no opportunity to use.

### A motorbike is slower than a man walking

A Bike is 1 × 2 UB — 4 × 6 studs, longest dimension 6. At `1.5×` that is **9 studs** per Action Point, against infantry's 12. It also costs 2 UB of Deployment Area (`DEP-003`) where an infantry model costs 1. It is strictly worse than walking.

### `1.5×` cannot be measured

| Vehicle | Longest dimension | Movement at 1.5× |
|---|---:|---:|
| Jeep (2 × 3 UB) | 9 | **13.5** |
| Tank (2 × 5 UB) | 15 | **22.5** |

There is no half stud. `07-movement.md`'s own Design Philosophy asks for movement that is "easy to measure" and "free from templates and measuring sticks", and this forces a fractional measurement onto a stud grid.

## What Changes

Two multipliers, and three paragraphs explaining what bounds them.

- **`VEH-004`** — vehicle movement becomes **3 × the vehicle's length**, replacing 1.5×.
- **`WPN-005`** — weapon Range becomes **Weapon Length × 6**, replacing × 2.
- **`CBT-003`** and **`docs/14-glossary.md`** — both restate the Range formula and must follow.
- **`WPN-005`** gains a paragraph on what bounds Range in practice, since the new figures look alarming without it.
- **`VEH-004`** gains the equivalent paragraph on clear lanes.

The mnemonic is one relationship: **move three, shoot six.** A weapon reaches twice as far as a vehicle of its own length can move.

### Resulting figures

| | Length | Move now | **Move (3×)** |
|---|---:|---:|---:|
| Bike | 6 | 9 | **18** |
| Buggy | 8 | 12 | **24** |
| Jeep | 9 | 13.5 | **27** |
| Tank | 15 | 22.5 | **45** |
| Heavy Transport | 24 | 36 | **72** |
| *Infantry, for comparison* | — | 12 | 12 |

| Platform | Longest weapon | Range now | **Range (6×)** |
|---|---:|---:|---:|
| Infantry (1 UB) | 4 | 8 | **24** |
| Bike | 6 | 12 | **36** |
| Jeep | 9 | 18 | **54** |
| Tank | 15 | 30 | **90** |

## Impact

**This is a mechanical change.** Every movement distance and every Range in the game changes. No rule ID is added, removed or renumbered, and no other mechanic is touched.

**Ranged combat starts working.** An infantry rifle reaches 24 studs — exactly two infantry moves. Closing from maximum range costs 2 Action Points and takes a round of fire on the way in. The shortest legal weapon (length 2, from `WPN-018`'s `Length ≥ 2 × Width` with a 1×1 muzzle) reaches 12, one full infantry move, which is a sensible floor.

**Bikes become vehicles again.** 18 studs against infantry's 12, so the 2 UB of Deployment Area buys something.

**Every distance is now an integer.** `3 × n` and `6 × n` are whole numbers for every whole n. The half-stud disappears.

**Movement stays proportional.** At 3×, every vehicle covers three of its own lengths per action regardless of size. A bike is not penalised for being small in relative terms — it is simply smaller.

**The Weapon Capacity trade-off gets three times sharper.** `WPN-004` caps the sum of mounted Weapon Lengths at Platform Length, so a Jeep (9) chooses between reach and rate of fire:

| Configuration | Range each | Weapon systems |
|---|---:|---:|
| One weapon of 9 | 54 | 1 |
| Two weapons of 4 | 24 | 2 |
| Three weapons of 3 | 18 | 3 |

The gap between the extremes widens from 18-vs-6 to 54-vs-18. A construction decision that already existed now carries three times the weight.

### No maximum, and why that is not an oversight

A Tank reaching 90 studs looks alarming, and a hypothetical super-heavy reaching further looks worse. No cap is added, for two reasons.

**The ruleset already answered this question.** `WPN-021` refused to cap Impact Strength, in the adjacent rule, deriving from the same Weapon Length: *"There is no maximum size... No component is unconditionally invulnerable; it is only safe from whatever can't be mounted on the attacker's current platform."* Capping Range would contradict that decision one rule away from where it was made.

**The cap already exists — it is just not a number.** There is a complete chain, every link either read from the model or agreed by the players:

```
Range  ≤ 6 × Weapon Length
       ≤ 6 × Platform Length              (WPN-004)
       ≤ what fits in the Deployment Area (SCS-003, DEP-003)
       ≤ the battlefield the players agreed (FLOW-001, step 2)
```

`FLOW-001` already requires agreeing the battlefield **before** the deployment size, so the order is designed for this. The numbers bear it out: the 3 × 10 UB super-heavy that would reach 180 studs costs 30 UB of Deployment Area and does not fit in a Skirmish (5 × 5 UB = 25 UB) at all. It needs a Battle, and a player running a Battle has the table for it.

**Range scales with the size of the game on its own.** Nothing needs to be written for that to happen.

What *is* added is a paragraph saying so, in the same shape `WPN-021` already uses to justify its own missing cap. A reader who calculates 90 studs and worries should find the answer in the rule, not have to reconstruct it.

**Line of sight is the practical limit.** `CORE-008` uses true physical visibility. A 90-stud Range only matters if 90 studs of clear sight exist, and on a table with terrain it does not. The same applies to movement: a 24-stud-long transport moving 72 studs needs a clear lane of nearly 100 studs, which terrain rarely allows.

### Not changed

- `MOVE-004` — infantry movement stays 12 studs. It is the reference every other figure is judged against, and nothing measured suggests it is wrong.
- `MEL-014` — melee reach is a physical contact check and has no multiplier to rescale.
- `WPN-004` — Weapon Capacity is unchanged; only the value derived from length changes.
- `WPN-021` — Impact Strength is unchanged. This proposal rescales *reach*, not *power*.

Not applied — proposal only.

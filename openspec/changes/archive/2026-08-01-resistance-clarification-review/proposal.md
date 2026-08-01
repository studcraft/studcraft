## Why

`delete-me-comments.md` is an external review of Resistance measurement, raising six points. Verified against the currently shipped ruleset, five are already implemented — `DMG-003` already defines the plate-layer unit, `DMG-008` already forbids material-specific mechanics, `SCS-023` already routes transparent components through the universal Geometry Check, and `DMG-017` is already generic. The review's remaining suggestion ("Resistance must always be measured in Plates, never in Bricks", stated with no exception) cannot be applied literally as written, because the current `DMG-003` deliberately carves out a fixed-piece exception for the minifig.

Investigating that exception surfaced the actual defect, which is larger than the review's scope.

**The Geometry Check compares two numbers measured in different units.**

```
DMG-014:   Impact Strength   ≥   Resistance
                  ↑                   ↑
           muzzle width          material crossed
           in studs              in plate layers
```

`WPN-021` derives Impact Strength from a muzzle's width in studs. `DMG-003` derives Resistance from the count of plate layers an Impact must cross. These are not the same unit, so the comparison is arbitrary rather than physical — and the resulting numbers are badly scaled against each other:

- Infantry are capped at Impact Strength 2 by construction (`WPN-004` Platform Length 4 → `WPN-018` Width ≤ 2 → `WPN-019` footprint 2×2 → `WPN-020` muzzle ≤ 2×2 → `WPN-021` Strength 2).
- Any component built from bricks has Resistance 3 (`DMG-004` Example 3).
- Therefore, by `DMG-014`, **no infantry weapon in the game can damage a brick-built wall, door, shield, or vehicle hull.** The Impact ends with no dice rolled.
- The same arithmetic applied to a real minifig (roughly one brick of material thick) would make every minifig immune to every infantry weapon.

The minifig exception in `DMG-003` was introduced to patch that last consequence. It works, but it treats the symptom: it rescues the one case where the mismatch was visible while leaving the mismatch itself — and every other affected component — in place. It also introduces the only measurement exception in the entire ruleset, against Principle 11 (Simplicity Before Complexity) and Principle 15 (avoid parallel systems).

## What Changes

**Align both sides of the Geometry Check on one unit, then delete the exception.**

One stud of muzzle width represents one brick of penetrating power, and a brick is 3 plate layers:

```
Impact Strength = muzzle size × 3
```

Both sides of `Strength ≥ Resistance` are now counts of plate layers. The comparison becomes physical instead of arbitrary, and the minifig stops needing special treatment — measured normally it is roughly one brick of material, Resistance 3, and a 1×1 muzzle now generates exactly Strength 3.

- `docs/10-weapons.md` **WPN-021**: Impact Strength becomes `muzzle size × 3` (`1×1` → 3, `2×2` → 6, `N×N` → 3N). Add the unit rationale: one stud of muzzle equals one brick of material equals 3 plate layers.
- `docs/16-damage-system.md` **DMG-003**: delete the fixed-piece exception entirely. Every component — constructed or moulded — is measured the same way: the plate-equivalent thickness of material an Impact must cross. State the conversion once (plate = 1, brick = 3, any other element = the plate-equivalent of its own thickness in the direction of travel).
- `docs/16-damage-system.md` **DMG-004**: Example 1 (Minifig) becomes a normal measurement (`Resistance 3`, roughly one brick of material) instead of a baseline. Add Example 5 (Bunker, 2 bricks → Resistance 6, per the reviewer's REVIEW-003 suggestion) and Example 6 (a moulded element — windscreen, wheel, accessory shield — measured by the same conversion, demonstrating that no exception is needed).
- `docs/16-damage-system.md` **DMG-008**: remove the "or, for a fixed piece like a minifig, its set baseline" clause — no longer true.
- `docs/16-damage-system.md` **DMG-017** and the four Combat Examples: renumber to the new scale.
- `docs/12-melee.md` **MEL-008**: unarmed attacks stop hardcoding `Impact Strength 1` and instead count as a size-1 striking end, inheriting Strength 3 from `WPN-021` — one less standalone number.
- `docs/15-geometry-layers.md` **GEO-001**: remove the "for constructed components only; a fixed piece like a minifig uses a set baseline" clause.
- `docs/14-glossary.md`: update `Impact Strength`, `Muzzle Size`, and `Resistance`.

## Impact

**Mechanical change — this is a rebalance, not a clarification.** Every Impact Strength in the game triples. Resistance values are unchanged.

Resolved by this change:

| Case | Before | After |
|---|---|---|
| Pistol (1×1) vs minifig | Impossible without the exception | `3 ≥ 3` ✓ |
| Infantry (max 2×2) vs brick shield (R 3) | `2 < 3` — impossible | `6 ≥ 3` ✓ |
| Infantry vs brick wall or door (R 3) | Impossible | ✓ |
| Infantry vs 4-plate shield (R 4) | Impossible | `6 ≥ 4` ✓ |
| Infantry vs bunker, 2 bricks (R 6) | Impossible | `6 ≥ 6` ✓ exactly |
| Tank (4×4) vs bunker (R 6) | `4 < 6` — impossible | `12 ≥ 6` ✓, 6 remaining |
| Moulded windscreen, wheel, shield accessory | Undefined | Measured like everything else ✓ |

Accepted consequences:

- **Penetration reaches deeper.** `DMG-017` subtracts Resistance from a tripled Strength, so large weapons pass through more layers. This is intended — a tank round should defeat a shield and the crew behind it — and each component still rolls its own independent Damage Roll (`DMG-015`), so depth increases exposure, not certainty.
- **Exact-threshold cases become common by design.** Pistol vs minifig and infantry-max vs bunker both land on `Strength = Resistance`. `DMG-014` already resolves ties in the attacker's favour (`≥`), and these are the intended breakpoints of the scale, not accidents.
- Impact Strength numbers get larger. No rule reads Impact Strength other than `DMG-014` and `DMG-017`, both of which are pure comparison and subtraction, so nothing else is affected.

No rule ID is added, removed, or renumbered. Not yet applied — proposal only.

**Note on this change's name:** the directory and branch retain the original `resistance-clarification-review` name from when the scope was limited to answering the external review. The scope is now the unit alignment described above.

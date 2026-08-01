## Why

Vehicle terrain interaction is a declared gap in two places. `docs/07-movement.md`'s Vehicle Movement section says outright that "`08-vehicles.md` currently has no equivalent to MOVE-009 through MOVE-016", and `MOVE-016` repeats it for falling. Infantry have four rules covering obstacles, slopes, stairs and vertical access; vehicles have none, and every question is currently resolved by table consensus.

The gap has an answer that needs no new statistic, because every locomotion type already carries its own threshold on the model:

- A wheel cannot climb an obstacle taller than its own axle. That is real vehicle geometry, and on a LEGO model the axle height *is* the wheel's radius — readable at a glance.
- A walker steps over what its knee clears. The knee joint is a visible, built component.
- A hover vehicle clears whatever fits under it. Its ground clearance is literally how high the builder floated the hull.

Each threshold is measured off the model rather than assigned, and each produces a different terrain profile as a consequence of construction — which is what Principle 1 asks for.

## What Changes

Six new rules in `docs/08-vehicles.md`, mirroring the structure `VEH-008` … `VEH-011` already uses (one rule per locomotion type, framed by a general one).

- **`VEH-021` — Terrain Threshold.** The general principle: every vehicle has a single Terrain Threshold read from its locomotion, measured in plate layers (`16-damage-system.md`, DMG-003). An obstacle taller than the threshold blocks movement; a drop deeper than it strands the vehicle.
- **`VEH-022` — Wheeled and Tracked Vehicles.** Threshold is axle height — equivalently, the wheel or road wheel's radius. Where a track build shows no axle, use half the height of the track run.
- **`VEH-023` — Walkers.** Threshold is knee height. Where a leg has no distinct knee joint, use half the leg's standing height.
- **`VEH-024` — Hover Vehicles.** Threshold is ground clearance — the gap between the hull's underside and the ground as built. Hover vehicles are **never stranded by a drop**: they pass over depressions entirely, provided the gap is narrower than the vehicle's own footprint.
- **`VEH-025` — Stranded Vehicles.** A vehicle that enters a drop deeper than its Terrain Threshold becomes Immobilized, resolved by the existing `VEH-019`. No new state is introduced.
- **`VEH-026` — Vehicle Falling.** A fall no deeper than the Terrain Threshold does nothing. Beyond it, one D6 per complete brick fallen past the threshold, each an independent Damage Roll (`DMG-015`) applied to a component that touches the ground on landing — a wheel, a track, a foot. Crew and passengers are never harmed. Hover vehicles take no falling damage.

Supporting edits:

- `docs/07-movement.md` Vehicle Movement — the deferral note is narrowed. Obstacles, drops and falling are now defined; slopes, stairs and vertical access remain open, and the note must say so rather than implying the whole gap is closed. `MOVE-016`'s infantry-only line is repointed at `VEH-026`.
- `docs/05-construction-components.md` — `CMP-003`, `CMP-004`, `CMP-005` and `CMP-006` gain a cross-reference to their locomotion's threshold rule, matching the pointer style `CMP-004` already uses for `VEH-009`.
- `docs/14-glossary.md` — add `Terrain Threshold` and `Stranded`.

## Impact

**New mechanic, not a repair.** Vehicles gain terrain rules where they previously had none. Nothing existing changes behaviour: no infantry rule, no numeric value, and no existing rule ID is touched or renumbered.

**The trade-off between locomotion types is the point.** Each threshold falls out of how the model is built, and they do not rank cleanly:

| Locomotion | Typical threshold | Stranded by drops? |
|---|---|---|
| Wheeled / tracked | Wheel radius — usually the tallest of the three | Yes |
| Walker | Knee height — varies most with build | Yes |
| Hover | Ground clearance — usually the lowest | **Never** |

A jeep drives over a one-brick wall that stops a hover platform; the hover platform crosses a trench that strands the jeep. A walker built on tall legs beats both, at the cost of a silhouette that is easier to see and shoot (`CORE-008`).

**Hover's immunity is deliberate and bounded.** It cannot be stranded, but its obstacle threshold is typically the lowest in the game, and it still cannot cross a gap wider than its own footprint — there must be something under it to hover over.

**Falling reuses infantry's dice, not infantry's target.** `MOVE-016` cannot be copied across, because a minifig is one component and `DMG-001` says a vehicle is not. The dice are identical; what changes is that each failure lands on a component the model identifies — whatever touches the ground — rather than on "the unit". No Geometry Check and no Resistance, for the same reason infantry falling skips them: a fall has no attacker and no Impact Strength.

**Crew are never harmed, deliberately.** A closed transport can fall fifteen bricks and its eight passengers walk out unhurt. That is a simplification, and it is stated as one in the rule rather than left to look like an oversight. The case is rare — nobody drives their own transport off a cliff on purpose — and the real cost is the paragraph below.

**The interesting consequence needed no rule at all.** A vehicle at the bottom of a ravine is a trap: its passengers disembark normally, then meet the ravine's walls as ordinary terrain, and `MOVE-011` already requires a slope, stair or ramp for anything 7 plate layers or higher. Driving into a pit can strand a squad as effectively as it strands the vehicle, and that falls straight out of the existing infantry rules.

**Scope boundary, narrowed but not closed.** Slopes, stairs and vertical access for vehicles remain undefined — `08-vehicles.md` still has no equivalent to `MOVE-012`, `MOVE-013` or `MOVE-014`. Task 2.1 rewrites `07-movement.md`'s deferral note to say which gap closed and which three did not.

**Sequencing.** `movement-audit-repairs` (PR #33) converts infantry obstacle heights to plate layers. This change uses the same unit. If #33 lands first the two agree immediately; if this lands first, #33's conversion makes them agree. Neither edits the same lines.

**No spec delta.** `openspec/specs/` has no vehicle or movement capability. Recorded as follow-up, consistent with PR #33.

Not applied — proposal only.

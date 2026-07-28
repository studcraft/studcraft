## Why

StudCraft already has a weapon ruleset (`docs/10-weapons.md`, WPN-001 through WPN-017), but several of its rules are narrower than the "Model Is The Rules" principle requires: muzzles are locked to a single fixed part (round 1×1), rate of fire is the only thing muzzles determine, and there is no notion of muzzle *size* driving impact. This proposal refines that ruleset so every offensive property (Range, Attack Dice, Impact Strength) is derived purely from measurable geometry, closing the gap between the stated philosophy and the current rules.

## What Changes

- Introduce weapon construction rules: every weapon is built from a single continuous **Weapon Body** with exactly one **Weapon Front**.
- Derive **Range** from Weapon Length (`Range = 2 × Weapon Length`).
- Derive **Attack Dice** from the number of muzzles (one die per muzzle).
- Derive **Impact Strength** from muzzle size (muzzles must be square: 1×1, 2×2, 3×3, 4×4 — rectangular muzzles invalid). Replaces the existing fixed round-1×1-only muzzle definition.
- **BREAKING**: Removes the mandatory 1-stud muzzle separation rule (existing WPN-007). The Weapon Front Footprint partition model permits directly adjacent muzzles (see the Twin/Quad Barrel examples), which WPN-007 would otherwise invalidate.
- **BREAKING**: Redefines Weapon Length as the longest dimension of the (functional, non-decorative) Weapon Body, replacing the existing "rear of body to foremost functional muzzle" measurement (WPN-003).
- Constrain weapon proportions: `Weapon Length ≥ 2 × Weapon Width` (new constraint, no prior equivalent).
- Define the **Weapon Front Footprint** (a `Weapon Width × Weapon Width` square) as the buildable area for muzzle placement, with rules for valid muzzle partitioning (square, non-overlapping, fully inside footprint, partial coverage allowed).
- Introduce **Weapon Capacity** per platform: `Σ(Weapon Length) ≤ Platform Length`, where Platform Length is the largest dimension of the unit base or vehicle. Generalizes the existing single-weapon max-length rule (WPN-004), which becomes the one-weapon special case of this constraint.
- No weapon classes/archetypes (rifle, cannon, machine gun, etc.) are modeled as data — they emerge purely from construction choices.
- Explicitly out of scope for this change: impact generation, armor interaction, penetration, damage resolution, area effects (reserved for future specs).

## Capabilities

### New Capabilities
- `weapon-construction`: Physical construction rules for weapons — Weapon Body, Weapon Front, Weapon Front Footprint, muzzle placement, and the derivation of Range, Attack Dice, and Impact Strength from geometry.
- `weapon-capacity`: Platform-level constraint governing how much total Weapon Length a platform (infantry, vehicle, etc.) may mount, based on Platform Length.

### Modified Capabilities
(none — no existing specs in `openspec/specs/`)

## Impact

- Affected documents: `docs/10-weapons.md` (rewrites WPN-002, WPN-003, WPN-004, WPN-006; removes WPN-007; updates Summary), `docs/14-glossary.md` (new terms), `CHANGELOG.md` (Unreleased entry, `**Bump:** major` — this is a breaking change to existing muzzle/length rules), `delete-me.md` (removed once formalized here). `docs/08-vehicles.md` and `docs/12-melee.md` are checked but expected to need no changes (scoped to ranged weapons only).
- Affected systems: weapon modeling/validation logic (new), unit/platform data model (needs Platform Length concept), any future combat resolution system (will consume Range/Attack Dice/Impact Strength as inputs).
- Existing constructions built under WPN-002/WPN-003/WPN-007 (fixed round-1×1 muzzles, rear-to-muzzle length, mandatory muzzle separation) may need re-measurement under the new rules.
- Downstream impact generation, armor, and damage resolution are intentionally deferred to future OpenSpec changes.

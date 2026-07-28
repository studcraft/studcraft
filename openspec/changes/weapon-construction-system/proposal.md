## Why

StudCraft currently has no defined mechanism for weapon behaviour. Without a construction system, weapons would need predefined stat profiles, which contradicts the core design principle: **The Model Is The Rules**. This proposal defines how a physical LEGO weapon model directly produces gameplay stats (Range, Attack Dice, Impact Strength), so no hidden or hand-authored weapon data is ever needed.

## What Changes

- Introduce weapon construction rules: every weapon is built from a single continuous **Weapon Body** with exactly one **Weapon Front**.
- Derive **Range** from Weapon Length (`Range = 2 × Weapon Length`).
- Derive **Attack Dice** from the number of muzzles (one die per muzzle).
- Derive **Impact Strength** from muzzle size (muzzles must be square: 1×1, 2×2, 3×3, 4×4 — rectangular muzzles invalid).
- Constrain weapon proportions: `Weapon Length ≥ 2 × Weapon Width`.
- Define the **Weapon Front Footprint** (a `Weapon Width × Weapon Width` square) as the buildable area for muzzle placement, with rules for valid muzzle partitioning (square, non-overlapping, fully inside footprint, partial coverage allowed).
- Introduce **Weapon Capacity** per platform: `Σ(Weapon Length) ≤ Platform Length`, where Platform Length is the largest dimension of the unit base or vehicle.
- No weapon classes/archetypes (rifle, cannon, machine gun, etc.) are modeled as data — they emerge purely from construction choices.
- Explicitly out of scope for this change: impact generation, armor interaction, penetration, damage resolution, area effects (reserved for future specs).

## Capabilities

### New Capabilities
- `weapon-construction`: Physical construction rules for weapons — Weapon Body, Weapon Front, Weapon Front Footprint, muzzle placement, and the derivation of Range, Attack Dice, and Impact Strength from geometry.
- `weapon-capacity`: Platform-level constraint governing how much total Weapon Length a platform (infantry, vehicle, etc.) may mount, based on Platform Length.

### Modified Capabilities
(none — no existing specs in `openspec/specs/`)

## Impact

- Affected: weapon modeling/validation logic (new), unit/platform data model (needs Platform Length concept), any future combat resolution system (will consume Range/Attack Dice/Impact Strength as inputs).
- No existing code or specs are modified; this is additive groundwork for combat mechanics.
- Downstream impact generation, armor, and damage resolution are intentionally deferred to future OpenSpec changes.

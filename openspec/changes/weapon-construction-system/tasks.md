## 1. Reconcile With Existing Ruleset

- [x] 1.1 Diff this proposal's `weapon-construction` spec against `docs/10-weapons.md`. Resolution per rule:
      - WPN-002 (Functional Muzzle) — **superseded**: fixed round-1×1-only definition replaced by square muzzles 1×1–4×4.
      - WPN-003 (Weapon Length) — **superseded**: "rear of body to foremost functional muzzle" replaced by "longest dimension of the functional Weapon Body" (decorative elements still excluded either way).
      - WPN-005 (Weapon Range), WPN-006 (Rate of Fire) — **compatible**, formulas unchanged.
      - WPN-007 (Muzzle Separation) — **removed**: the footprint partition model permits directly adjacent muzzles (see Twin/Quad Barrel examples in the spec), which the 1-stud-separation rule would otherwise invalidate.
      - Weapon Proportion Constraint (`Length ≥ 2 × Width`) and Weapon Front Footprint — **new**, no existing counterpart.
- [x] 1.2 Diff this proposal's `weapon-capacity` spec against `docs/10-weapons.md` (WPN-004) to confirm the new `Σ(Weapon Length) ≤ Platform Length` rule generalizes the existing single-max-length rule without contradicting it.
- [x] 1.3 Confirm Platform Length aligns with the existing Unit Base (UB) concept defined in `docs/01-foundations.md` and `docs/02-core-rules.md`.

## 2. Update Ruleset Docs (`/docs`)

- [x] 2.1 Update `docs/10-weapons.md`: replace WPN-002 (Functional Muzzle) to define square muzzles (1×1 through 4×4) and remove the fixed round-plate/round-brick-only definition.
- [x] 2.2 Update WPN-003 (Weapon Length) to the new "longest dimension of the functional Weapon Body, excluding decorative elements" measurement.
- [x] 2.3 Remove WPN-007 (Muzzle Separation) entirely, or replace it with an explicit note that muzzles may be directly adjacent (only overlap is forbidden) — do not leave it silently contradicted by the new footprint rules.
- [x] 2.4 Add a new numbered rule for Muzzle Size → Impact Strength, and update WPN-006 (Rate of Fire) to clarify each muzzle still grants exactly one Attack Die regardless of size.
- [x] 2.5 Add a new numbered rule defining the Weapon Front Footprint (Weapon Width × Weapon Width) and muzzle placement validity (square, non-overlapping, fully inside footprint, partial coverage allowed, direct adjacency allowed).
- [x] 2.6 Add a new numbered rule for the Weapon Proportion Constraint (`Length ≥ 2 × Width`).
- [x] 2.7 Update WPN-004 (Maximum Weapon Length) to state the full Weapon Capacity constraint (`Σ(Weapon Length) ≤ Platform Length`) instead of a single max-length statement, with infantry and vehicle examples from the spec.
- [x] 2.8 Update the Summary section of `docs/10-weapons.md` to reflect the three physical properties (Length, Muzzle Count, Muzzle Size) and remove any now-inaccurate statements.
- [x] 2.9 Add or update Weapon Archetypes examples (Rifle, Machine Gun, Cannon, Rocket Launcher, Naval Battery) as illustrative, non-normative guidance.

## 3. Glossary and Cross-References

- [x] 3.1 Add/update entries in `docs/14-glossary.md` for: Weapon Body, Weapon Front, Weapon Front Footprint, Muzzle Size, Impact Strength, Weapon Capacity, Platform Length.
- [x] 3.2 Check `docs/08-vehicles.md` for any weapon-mounting references that need to reflect the new Weapon Capacity rule.
- [x] 3.3 Check `docs/12-melee.md` to confirm melee striking-end rules remain unaffected (this change is scoped to ranged weapons only).

## 4. Validation

- [x] 4.1 Walk through every example in the `weapon-construction` and `weapon-capacity` specs (Twin Barrel, Quad Barrel, Heavy Cannon, Hybrid; Infantry and Jeep capacity cases) against the updated `docs/10-weapons.md` text to confirm consistency.
- [x] 4.2 Confirm no requirement introduces impact generation, armor interaction, penetration, damage resolution, or area effects (explicitly out of scope).

## 5. Housekeeping

- [x] 5.1 Add a `CHANGELOG.md` entry under `[Unreleased]` summarizing the weapon construction/capacity rule update, including a `**Bump:** major` line (required by the `Docs require changelog bump` CI check — this is a breaking change: it removes WPN-007 and redefines WPN-003's measurement method).
- [x] 5.2 Remove `delete-me.md` from the repo root now that its content has been formalized into this OpenSpec change.
- [x] 5.3 Open a PR from the `weapon-construction-system` branch for review before archiving this change.

## Why

StudCraft's existing rules (`docs/10-weapons.md`, `docs/08-vehicles.md`, etc.) already measure specific properties — Weapon Length, Muzzle Size, Platform Length — but never state which parts of a LEGO model those measurements come from, or what the rest of the model is allowed to be. Without that distinction, "The Model Is The Rules" is ambiguous: does a decorative antenna change a weapon's Range? Does a greebled hull panel change a vehicle's Weapon Capacity? This proposal formalizes the two-layer split (Gameplay Geometry vs. Visual Geometry) so players and future rules have one consistent answer.

## What Changes

- Every model splits into two layers: **Gameplay Geometry** (measurable properties that feed rule values — Weapon Length, Weapon Width, Muzzle Count, Muzzle Sizes, Platform footprint/dimensions, Transport volume, Movement geometry) and **Visual Geometry** (everything else — slopes, pipes, Technic details, decorative armor, exhausts, antennas, greebling, printed parts, colors, cosmetic plates).
- Visual Geometry never contributes to any measured rule value (Range, Attack Dice, Impact Strength, Weapon Capacity, Transport Capacity, Movement distance) — those are always computed from Gameplay Geometry alone.
- Visual Geometry **does** still count for direct physical checks that already exist and are not measured values: Line of Sight (`02-core-rules.md` CORE-008/CORE-009) and Cover (CORE-010). This is not a new exception — those rules already operate on "whatever can be physically seen/hidden," which visual decoration is part of. This proposal makes that consequence explicit instead of leaving it implicit and easy to misread as "decoration has zero effect, period."
- Introduces **Functional Equivalence**: two models with identical Gameplay Geometry produce identical measured values (Range, Attack Dice, Impact Strength, etc.) regardless of how different they look. Their Line of Sight/Cover outcomes can still differ if one is visually bulkier.
- Introduces **Minimum Representation**: every model has a valid build using only its required Gameplay Geometry, so a small LEGO collection is always enough to play.
- Introduces **Detailed Representation**: a model built with extra Visual Geometry on top of a valid Minimum Representation remains valid, as long as its Gameplay Geometry is unchanged — players can add detail without invalidating their build.
- No existing measured rule value changes as a result of this proposal — it names and formalizes a distinction the existing ruleset already relies on implicitly (e.g. `WPN-003`/`WPN-015`: "decorative elements are ignored" when measuring Weapon Length; `VEH-003`: same for vehicles).

## Capabilities

### New Capabilities
- `geometry-layers`: Defines the Gameplay Geometry / Visual Geometry split, what belongs to each layer, Functional Equivalence, Minimum Representation, and the Line of Sight/Cover carve-out for Visual Geometry.

### Modified Capabilities
- `weapon-construction`: The "Weapon Length Determines Range" requirement's decorative-exclusion scenario is reworded to reference the `geometry-layers` split (Visual Geometry) by name, instead of asserting "decorative elements are ignored" independently. No measured behavior changes — this is a terminology-alignment edit only, so the two capabilities don't end up independently asserting the same rule in different words.

## Impact

- Affected documents: likely a new `docs/*.md` file (or a new section in an existing foundational doc — see design.md) defining Gameplay vs. Visual Geometry; `docs/14-glossary.md` (new terms: Gameplay Geometry, Visual Geometry, Functional Equivalence, Minimum Representation, Detailed Representation). No `CHANGELOG.md` edit is needed — release-cut computes the bump automatically from git history (see `system/workflow.md`); this being purely additive/clarifying would default to the standard minor bump.
- `docs/10-weapons.md` gets a light wording edit (WPN-003, to reference `geometry-layers` terminology instead of standalone "decorative elements" — see Modified Capabilities above); no measured rule value or formula changes anywhere. `docs/08-vehicles.md` may get an optional cross-reference (VEH-003) but no content change.
- Affects future rule-writing: any future OpenSpec proposal that introduces a new measured value must classify its inputs as Gameplay Geometry, and must not let Visual Geometry silently affect it.

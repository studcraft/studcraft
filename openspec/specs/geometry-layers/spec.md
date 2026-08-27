# geometry-layers Specification

## Purpose
TBD - created by archiving change gameplay-visual-geometry. Update Purpose after archive.

## Requirements

### Requirement: Geometry Layer Split
Every model SHALL be classified into two layers: Gameplay Geometry and Visual Geometry. Gameplay Geometry SHALL consist only of measurable properties that feed a rule's measured value. Visual Geometry SHALL consist of every other physical element.

A plate or panel SHALL count as Visual Geometry only if it is not part of the structural cross-section an Impact must cross. A plate that does sit in that cross-section SHALL be Gameplay Geometry however decorative it looks, and SHALL contribute to the component's Resistance.

#### Scenario: Model splits into two layers
- **WHEN** a player builds any weapon, vehicle, or building
- **THEN** every physical element of that model belongs to exactly one of Gameplay Geometry or Visual Geometry

### Requirement: Gameplay Geometry Determines Measured Values
Only Gameplay Geometry SHALL be used when computing a measured rule value: Range, Attack Dice, Impact Strength, Resistance, Weapon Capacity, Transport Capacity, and Movement distance. Visual Geometry SHALL NOT contribute to any of these values.

Component structural thickness SHALL be part of Gameplay Geometry, measured the same way for every component whether moulded or built.

#### Scenario: Decorative element does not change a measured value
- **WHEN** a weapon has a decorative antenna, exhaust, or greebling attached that is not part of its Weapon Body, Weapon Front, or muzzles
- **THEN** the weapon's Range, Attack Dice, and Impact Strength are computed exactly as if the decorative element were absent

#### Scenario: Bolted-on decorative armour does not add Resistance
- **WHEN** a decorative plate is attached on top of a component's structural wall rather than forming part of it
- **THEN** it does not increase that component's Resistance

#### Scenario: A decorative-looking plate inside the cross-section does count
- **WHEN** a plate sits within the structural cross-section an Impact must cross, however decorative it appears
- **THEN** it is Gameplay Geometry and contributes to Resistance

### Requirement: Visual Geometry Still Applies to Physical Checks
Visual Geometry SHALL be considered, together with Gameplay Geometry, whenever a rule is a direct physical check against the model rather than a measured value. This applies at minimum to Line of Sight, Cover, and whether an access point's opening passes the models that use it.

#### Scenario: Decoration blocks line of sight
- **WHEN** a decorative element physically obstructs the view between an attacker and a target
- **THEN** the target is not visible, exactly as if the obstruction were part of Gameplay Geometry

#### Scenario: Decoration can complete concealment
- **WHEN** a decorative element physically hides a component completely from an attacker's viewpoint
- **THEN** that component cannot be selected as a target, exactly as if the obstruction were part of Gameplay Geometry — Cover is binary and grants no bonus for partial concealment

#### Scenario: Decoration narrows an access opening
- **WHEN** decorative elements around a door, hatch or portal reduce the opening so that a model which would otherwise fit can no longer be passed through it
- **THEN** that access point is decorative for that model and has no gameplay effect, exactly as if the obstruction were part of Gameplay Geometry

### Requirement: Functional Equivalence
Two models with identical Gameplay Geometry SHALL produce identical measured values, regardless of differences in Visual Geometry. This equivalence does not extend to physical checks (Line of Sight, Cover), which may still differ based on Visual Geometry.

#### Scenario: Identical Gameplay Geometry produces identical measured values
- **WHEN** two weapons have the same Weapon Length, Weapon Width, Muzzle Count, and Muzzle Sizes but different Visual Geometry
- **THEN** both weapons have identical Range, Attack Dice, and Impact Strength

#### Scenario: Visual Geometry may still change a physical-check outcome
- **WHEN** two otherwise-Functionally-Equivalent weapons differ in Visual Geometry bulk
- **THEN** their Line of Sight and Cover outcomes are permitted to differ

### Requirement: Minimum Representation
Every model SHALL have a valid minimum representation consisting only of the Gameplay Geometry required by the rules, with no Visual Geometry. This SHALL be stated by the same rule that states Functional Equivalence, since a minimum representation is the case of that equivalence with one side empty.

#### Scenario: Minimum representation is playable
- **WHEN** a player builds a model containing only the Gameplay Geometry required for its type (e.g. Weapon Body, Weapon Front, muzzles for a weapon)
- **THEN** the model is fully valid and playable

### Requirement: Detailed Representation
A model built with Visual Geometry added on top of a valid Minimum Representation SHALL remain valid, provided its Gameplay Geometry is unchanged. A model SHALL NOT become invalid, and its measured values SHALL NOT change, solely as a result of adding Visual Geometry. This SHALL be stated by the same rule that states Minimum Representation, so that the two halves of one permission are read together.

#### Scenario: Adding detail preserves validity
- **WHEN** a player adds Visual Geometry (e.g. slopes, printed parts, greebling) to an already-valid model without altering its Gameplay Geometry
- **THEN** the model remains valid

#### Scenario: Adding detail does not change measured values
- **WHEN** a player adds Visual Geometry to an already-valid model without altering its Gameplay Geometry
- **THEN** every measured value of that model (Range, Attack Dice, Impact Strength, Resistance, Weapon Capacity, Transport Capacity, Movement distance) stays exactly the same

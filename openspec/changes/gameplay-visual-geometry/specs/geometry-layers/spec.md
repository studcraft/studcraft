## ADDED Requirements

### Requirement: Geometry Layer Split
Every model SHALL be classified into two layers: Gameplay Geometry and Visual Geometry. Gameplay Geometry SHALL consist only of measurable properties that feed a rule's measured value. Visual Geometry SHALL consist of every other physical element.

#### Scenario: Model splits into two layers
- **WHEN** a player builds any weapon, vehicle, or building
- **THEN** every physical element of that model belongs to exactly one of Gameplay Geometry or Visual Geometry

### Requirement: Gameplay Geometry Determines Measured Values
Only Gameplay Geometry SHALL be used when computing a measured rule value: Range, Attack Dice, Impact Strength, Weapon Capacity, Transport Capacity, and Movement distance. Visual Geometry SHALL NOT contribute to any of these values.

#### Scenario: Decorative element does not change a measured value
- **WHEN** a weapon has a decorative antenna, exhaust, or greebling attached that is not part of its Weapon Body, Weapon Front, or muzzles
- **THEN** the weapon's Range, Attack Dice, and Impact Strength are computed exactly as if the decorative element were absent

### Requirement: Visual Geometry Still Applies to Physical Checks
Visual Geometry SHALL be considered, together with Gameplay Geometry, whenever a rule is a direct physical check against the model rather than a measured value. This applies at minimum to Line of Sight and Cover.

#### Scenario: Decoration blocks line of sight
- **WHEN** a decorative element physically obstructs the view between an attacker and a target
- **THEN** the target is not visible, exactly as if the obstruction were part of Gameplay Geometry

#### Scenario: Decoration provides cover
- **WHEN** a decorative element physically hides part of a model from an attacker's viewpoint
- **THEN** that portion of the model counts toward Cover, exactly as if it were part of Gameplay Geometry

### Requirement: Functional Equivalence
Two models with identical Gameplay Geometry SHALL produce identical measured values, regardless of differences in Visual Geometry. This equivalence does not extend to physical checks (Line of Sight, Cover), which may still differ based on Visual Geometry.

#### Scenario: Identical Gameplay Geometry produces identical measured values
- **WHEN** two weapons have the same Weapon Length, Weapon Width, Muzzle Count, and Muzzle Sizes but different Visual Geometry
- **THEN** both weapons have identical Range, Attack Dice, and Impact Strength

#### Scenario: Visual Geometry may still change a physical-check outcome
- **WHEN** two otherwise-Functionally-Equivalent weapons differ in Visual Geometry bulk
- **THEN** their Line of Sight and Cover outcomes are permitted to differ

### Requirement: Minimum Representation
Every model SHALL have a valid minimum representation consisting only of the Gameplay Geometry required by the rules, with no Visual Geometry.

#### Scenario: Minimum representation is playable
- **WHEN** a player builds a model containing only the Gameplay Geometry required for its type (e.g. Weapon Body, Weapon Front, muzzles for a weapon)
- **THEN** the model is fully valid and playable

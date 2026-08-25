# geometry-layers Specification Delta

`GEO-006` and `GEO-007` are retired. **Neither requirement below loses anything
it stated** — both are now carried by `GEO-005`, which already owned Functional
Equivalence and is where a reader looking for "does adding detail break my
model?" arrives. What changes is the owning rule, and the wording follows it.

## MODIFIED Requirements

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

# weapon-capacity Specification

## Purpose
TBD - created by archiving change weapon-construction-system. Update Purpose after archive.
## Requirements
### Requirement: Platform Length Definition
Platform Length SHALL be the largest horizontal dimension of the platform's Unit Base or vehicle bounding box. The Unit Base's height SHALL NOT be a candidate for Platform Length.

#### Scenario: Platform length from bounding box
- **WHEN** a vehicle platform has a base of 8×9
- **THEN** its Platform Length is 9

#### Scenario: Infantry Platform Length ignores the Unit Base's height
- **WHEN** an infantry platform of one Unit Base is measured
- **THEN** its Platform Length is 4 studs, and the Unit Base's height is not considered

### Requirement: Weapon Capacity Constraint
The sum of the Weapon Length of every weapon mounted on a platform SHALL NOT exceed that platform's Platform Length (`Σ(Weapon Length) ≤ Platform Length`).

#### Scenario: Single weapon at capacity accepted
- **WHEN** a platform with Platform Length 4 mounts one weapon of Weapon Length 4
- **THEN** the load-out is valid

#### Scenario: Multiple weapons within capacity accepted
- **WHEN** a platform with Platform Length 4 mounts two weapons of Weapon Length 2 each
- **THEN** the load-out is valid

#### Scenario: Mixed-length weapons within capacity accepted
- **WHEN** a platform with Platform Length 4 mounts one weapon of Weapon Length 3 and one weapon of Weapon Length 1
- **THEN** the load-out is valid

#### Scenario: Load-out exceeding capacity rejected
- **WHEN** a platform with Platform Length 4 mounts two weapons of Weapon Length 4 each
- **THEN** the load-out is invalid

#### Scenario: Jeep-scale capacity accepted
- **WHEN** a platform with Platform Length 9 mounts one weapon of Weapon Length 5 and two weapons of Weapon Length 2 each
- **THEN** the load-out is valid

#### Scenario: Jeep-scale capacity exceeded rejected
- **WHEN** a platform with Platform Length 9 mounts three weapons of Weapon Length 4 each
- **THEN** the load-out is invalid


## MODIFIED Requirements

### Requirement: Muzzle Placement Validity
Every muzzle SHALL be round and SHALL fit entirely inside the Weapon Front Footprint, occupying a square footprint slot (the same way a round LEGO plate or tile occupies a square footprint of studs). Muzzles SHALL NOT overlap one another. Unused footprint space is allowed; muzzles are not required to cover the entire footprint. Square or rectangular muzzles SHALL be considered invalid.

#### Scenario: Round muzzle accepted
- **WHEN** a 2×2 round muzzle is placed fully within the Weapon Front Footprint without overlapping any other muzzle
- **THEN** the muzzle placement is valid

#### Scenario: Square muzzle rejected
- **WHEN** a square (non-round) piece is used to define a muzzle
- **THEN** the muzzle is invalid

#### Scenario: Rectangular muzzle rejected
- **WHEN** a muzzle with dimensions 1×2 is defined on the Weapon Front
- **THEN** the muzzle is invalid

#### Scenario: Overlapping muzzles rejected
- **WHEN** two muzzles occupy any of the same footprint cells
- **THEN** the construction is invalid

#### Scenario: Muzzle exceeding footprint rejected
- **WHEN** a muzzle extends beyond the boundary of the Weapon Front Footprint
- **THEN** the construction is invalid

#### Scenario: Partial footprint coverage accepted
- **WHEN** a weapon's muzzles occupy fewer cells than the total Weapon Front Footprint
- **THEN** the construction remains valid

#### Scenario: Directly adjacent muzzles accepted
- **WHEN** two round muzzles share an edge with no gap of Weapon Body between them
- **THEN** the placement is valid, since only overlap is forbidden, not adjacency

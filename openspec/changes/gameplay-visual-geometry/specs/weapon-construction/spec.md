## MODIFIED Requirements

### Requirement: Weapon Length Determines Range
Weapon Length SHALL be measured as the longest dimension of the functional Weapon Body, excluding Visual Geometry (per the `geometry-layers` capability). Range SHALL be derived as `Range = 2 × Weapon Length`.

#### Scenario: Range computed from length
- **WHEN** a weapon has a Weapon Length of N
- **THEN** its Range is 2 × N

#### Scenario: Visual Geometry excluded from length
- **WHEN** a Visual Geometry element extends beyond the functional Weapon Body
- **THEN** that element is not counted when measuring Weapon Length

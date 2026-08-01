## MODIFIED Requirements

### Requirement: Weapon Length Determines Range
Weapon Length SHALL be measured as the longest dimension of the functional Weapon Body, along the weapon's firing axis — the axis running perpendicular to the Weapon Front. Mounting hardware and decorative elements SHALL be excluded from the measurement. Range SHALL be derived as `Range = 2 × Weapon Length`.

#### Scenario: Range computed from length
- **WHEN** a weapon has a Weapon Length of N
- **THEN** its Range is 2 × N

#### Scenario: Decorative overhang excluded from length
- **WHEN** a decorative element extends beyond the functional Weapon Body
- **THEN** that decorative element is not counted when measuring Weapon Length

#### Scenario: Mounting hardware excluded from length
- **WHEN** a weapon is attached to its platform by a mount, pintle, or grip
- **THEN** that attachment is not part of the Weapon Body and is not counted when measuring Weapon Length

#### Scenario: Length is measured along the firing axis
- **WHEN** a Weapon Body's dimensions are measured
- **THEN** Weapon Length is the dimension running perpendicular to the Weapon Front, not merely the largest dimension in any arbitrary direction

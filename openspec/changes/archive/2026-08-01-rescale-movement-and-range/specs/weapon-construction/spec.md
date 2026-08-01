## MODIFIED Requirements

### Requirement: Weapon Length Determines Range
Weapon Length SHALL be measured as the longest dimension of the functional Weapon Body, along the weapon's firing axis — the axis running perpendicular to the Weapon Front. Mounting hardware and decorative elements SHALL be excluded from the measurement. Range SHALL be derived as `Range = 6 × Weapon Length`.

Range SHALL have no written maximum. Its bound is what the attacker's platform can carry: Weapon Length is limited by Platform Length, platform size by the agreed Deployment Area, and the Deployment Area by the battlefield the players agree on beforehand. Range therefore scales with the size of the game without a stated cap, for the same reason Impact Strength does.

Maximum Range SHALL NOT be assumed to be the practical limit, because Line of Sight is a physical check against the model and the battlefield.

#### Scenario: Range computed from length
- **WHEN** a weapon has a Weapon Length of N
- **THEN** its Range is 6 × N

#### Scenario: Range always resolves to a whole number of studs
- **WHEN** a weapon's Range is computed from any whole Weapon Length
- **THEN** the result is a whole number of studs, with no fractional distance to measure

#### Scenario: Decorative overhang excluded from length
- **WHEN** a decorative element extends beyond the functional Weapon Body
- **THEN** that decorative element is not counted when measuring Weapon Length

#### Scenario: Mounting hardware excluded from length
- **WHEN** a weapon is attached to its platform by a mount, pintle, or grip
- **THEN** that attachment is not part of the Weapon Body and is not counted when measuring Weapon Length

#### Scenario: A weapon outranges one infantry move
- **WHEN** an infantry model carries the longest weapon its platform permits (Weapon Length 4, from a Platform Length of 4)
- **THEN** its Range is 24 studs, two full infantry movement actions, so an approaching enemy is exposed to fire before reaching contact

#### Scenario: No maximum range is defined
- **WHEN** a platform large enough to carry an arbitrarily long weapon is built
- **THEN** its Range scales accordingly, bounded by Platform Length, Deployment Area and the agreed battlefield rather than by a stated maximum

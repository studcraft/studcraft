# weapon-construction Specification

## Purpose
TBD - created by archiving change weapon-construction-system. Update Purpose after archive.
## Requirements
### Requirement: Weapon Body Continuity
A weapon's Weapon Body SHALL consist of one continuous structure. Floating or disconnected barrel sections SHALL be considered an invalid construction.

#### Scenario: Continuous body accepted
- **WHEN** a weapon model is built as a single continuous structure
- **THEN** the model is a valid Weapon Body

#### Scenario: Disconnected barrel rejected
- **WHEN** a weapon model contains a muzzle section that is not physically connected to the rest of the Weapon Body
- **THEN** the construction is invalid

### Requirement: Single Weapon Front
Every weapon SHALL have exactly one Weapon Front, which is the only face from which the weapon may fire. Muzzles SHALL NOT be placed on the rear, side, top, or bottom faces of the weapon.

#### Scenario: Muzzles on front face only
- **WHEN** all muzzles of a weapon are located on a single designated face
- **THEN** that face is the Weapon Front and the construction is valid

#### Scenario: Muzzle on non-front face rejected
- **WHEN** a muzzle is placed on the rear, a side, the top, or the bottom face of the weapon
- **THEN** the construction is invalid

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

### Requirement: Weapon Proportion Constraint
Weapon Length SHALL be at least twice the Weapon Width (`Length ≥ 2 × Width`). Weapon Width is the smallest dimension of the Weapon Body.

#### Scenario: Valid proportion accepted
- **WHEN** a weapon has Length 8 and Width 4
- **THEN** the construction satisfies Length ≥ 2 × Width and is valid

#### Scenario: Invalid proportion rejected
- **WHEN** a weapon has Length 4 and Width 4
- **THEN** the construction violates Length ≥ 2 × Width and is invalid

### Requirement: Weapon Front Footprint
The Weapon Front SHALL be represented by a square construction area with dimensions `Weapon Width × Weapon Width`. This footprint SHALL define the only available space for muzzle placement.

#### Scenario: Footprint size matches width
- **WHEN** a weapon has Weapon Width 4
- **THEN** its Weapon Front Footprint is a 4×4 square area

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

### Requirement: Attack Dice From Muzzle Count
Every muzzle SHALL generate exactly one attack die. Attack Dice SHALL equal the number of muzzles on the Weapon Front.

#### Scenario: Attack dice computed from muzzle count
- **WHEN** a weapon has 4 valid muzzles on its Weapon Front
- **THEN** the weapon has 4 Attack Dice

### Requirement: Impact Strength From Muzzle Size
Impact Strength SHALL equal the size of the muzzle that generated the attack, multiplied by 3. One stud of muzzle width represents one brick of penetrating power, and a brick is 3 plate layers (`16-damage-system.md`, DMG-003), so Impact Strength and Resistance SHALL both be expressed as counts of plate layers and SHALL be directly comparable in the Geometry Check.

A muzzle of size N SHALL therefore generate Impact Strength 3N. There SHALL be no maximum: a larger Weapon Front Footprint supports a larger muzzle, with Impact Strength scaling accordingly.

The same rule SHALL apply to a melee weapon's functional striking end (`12-melee.md`, MEL-013), which is sized identically to a muzzle. An unarmed attack SHALL count as a size-1 striking end rather than stating its own literal Impact Strength.

#### Scenario: Impact strength computed from muzzle size
- **WHEN** a weapon has a 2×2 muzzle
- **THEN** the attack die generated by that muzzle has Impact Strength 6

#### Scenario: Smallest legal muzzle defeats one brick of material
- **WHEN** a weapon has a 1×1 muzzle
- **THEN** the attack die generated by that muzzle has Impact Strength 3, exactly the Resistance of a component one brick thick

#### Scenario: Mixed muzzle sizes produce independent impact strengths
- **WHEN** a weapon has one 2×2 muzzle and two 1×1 muzzles
- **THEN** it produces 3 Attack Dice with Impact Strengths 6, 3, and 3 respectively

#### Scenario: Infantry-carried weapons can affect brick-built components
- **WHEN** an infantry model carries a weapon with the largest muzzle its platform permits (2×2, per the Weapon Capacity and Weapon Proportion limits)
- **THEN** that weapon generates Impact Strength 6, which passes the Geometry Check against a component built from one brick (Resistance 3) or two bricks (Resistance 6)

#### Scenario: Unarmed attack derives its strength rather than stating one
- **WHEN** a unit attacks with no melee weapon
- **THEN** the attack counts as a size-1 striking end and generates Impact Strength 3


## MODIFIED Requirements

### Requirement: Unit Base Measurement
The Unit Base (UB) SHALL be StudCraft's universal measurement, equal to a volume measuring 4 studs wide, 3 studs deep and 13 plate layers tall. Thirteen plate layers SHALL equal exactly 4 standard bricks and one plate, and the height SHALL be measured from the underside of the base an infantry model stands on, which is part of the volume rather than the floor beneath it. That base SHALL be one physical base measuring 4 × 3 studs and one plate thick — the Unit Base read horizontally, and the plate counted in its height. Every distance, Deployment Volume, and vehicle or infantry footprint SHALL be expressed using this unit. Wherever a rule asks whether something physically fits, the volume that must fit SHALL be the Unit Base — one for a minifigure, its own volume in Unit Bases for a vehicle — and never the loose model.

#### Scenario: Unit Base dimensions
- **WHEN** a Unit Base is measured
- **THEN** it measures 4 studs wide, 3 studs deep and 13 plate layers tall

#### Scenario: Infantry occupies one Unit Base
- **WHEN** an infantry model is placed on its standard base
- **THEN** it occupies exactly one Unit Base, whether standing or seated, and never a fraction of one

#### Scenario: The standard base is the horizontal reading
- **WHEN** an infantry model is built
- **THEN** it stands on one physical base measuring 4 × 3 studs and one plate thick, and that plate is the one counted in the Unit Base's height

#### Scenario: Vehicle footprint measured in Unit Bases
- **WHEN** a vehicle's footprint is measured
- **THEN** it is expressed as a number of Unit Bases read from the horizontal projection, not an independent unit of measure

#### Scenario: What must fit is the Unit Base
- **WHEN** a rule asks whether a model fits inside a space
- **THEN** the space must admit the model's Unit Base volume, even where the loose model would slip into something smaller

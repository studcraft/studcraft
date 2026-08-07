# unit-base Specification

## Purpose
TBD - created by archiving change consolidate-core-measurements. Update Purpose after archive.
## Requirements
### Requirement: Unit Base Measurement
The Unit Base (UB) SHALL be StudCraft's universal measurement, equal to a volume measuring 4 studs wide, 3 studs deep and 12 plate layers tall. Twelve plate layers SHALL equal exactly 4 standard bricks, and the height SHALL be measured from the top face of the plate an infantry model stands on. Every distance, deployment area, and vehicle or infantry footprint SHALL be expressed using this unit. Wherever a rule asks whether something physically fits, the volume that must fit SHALL be the Unit Base — one for a minifigure, its own volume in Unit Bases for a vehicle — and never the loose model.

#### Scenario: Unit Base dimensions
- **WHEN** a Unit Base is measured
- **THEN** it measures 4 studs wide, 3 studs deep and 12 plate layers tall

#### Scenario: Infantry occupies one Unit Base
- **WHEN** an infantry model is placed on its standard base
- **THEN** it occupies exactly one Unit Base, whether standing or seated, and never a fraction of one

#### Scenario: Vehicle footprint measured in Unit Bases
- **WHEN** a vehicle's footprint is measured
- **THEN** it is expressed as a number of Unit Bases read from the horizontal projection, not an independent unit of measure

#### Scenario: What must fit is the Unit Base
- **WHEN** a rule asks whether a model fits inside a space
- **THEN** the space must admit the model's Unit Base volume, even where the loose model would slip into something smaller

### Requirement: Unit Base Projections
A rule SHALL read whichever projection of the Unit Base volume it requires: the horizontal projection (4 × 3 studs) for distances, movement, deployment areas and footprints; the volume itself for transport capacity and interior space; and the vertical projection across the front (4 studs × 12 plate layers) for whether something passes through an opening. A projection SHALL supply a measured value only. A projection SHALL NOT replace a physical check: Line of Sight and Cover SHALL be resolved against the physical model on the table, never against a Unit Base silhouette.

#### Scenario: Deployment reads the horizontal projection
- **WHEN** a vehicle's Deployment Area cost is computed
- **THEN** it is read from the horizontal projection of the Unit Bases it covers, and its height is not considered

#### Scenario: An opening is measured against the vertical projection
- **WHEN** an access opening is checked against an infantry model
- **THEN** the clear opening must measure at least 4 studs wide and 12 plate layers high

#### Scenario: Line of Sight is not traced against a projection
- **WHEN** visibility between an attacker and a target is resolved
- **THEN** it is resolved against the physical models on the table, and the Unit Base volume or any of its projections plays no part

### Requirement: Cargo Divides a Unit Base
Cargo SHALL be permitted to share one Unit Base, each object occupying a slice measuring 4 × 3 studs by its own height, with the slices sharing a Unit Base totalling no more than 12 plate layers. An object narrower than 4 × 3 studs SHALL still occupy a whole slice of its own height, and an object whose footprint covers more than one Unit Base SHALL occupy a slice of its own height in each Unit Base it covers. Infantry SHALL never share a Unit Base.

#### Scenario: Three short crates share one Unit Base
- **WHEN** three crates of 4 plate layers each are loaded
- **THEN** they occupy exactly one Unit Base together

#### Scenario: A crate never shares with a minifigure
- **WHEN** a 4-plate-layer crate and an infantry model are loaded
- **THEN** they occupy two Unit Bases, because the infantry model occupies a whole one on its own

#### Scenario: A narrow object still costs a whole slice
- **WHEN** an object narrower than 4 × 3 studs is loaded
- **THEN** it occupies a slice 4 × 3 studs wide by its own height


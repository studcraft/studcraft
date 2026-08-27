# unit-base Specification

## Purpose
TBD - created by archiving change consolidate-core-measurements. Update Purpose after archive.

## Requirements

### Requirement: Unit Base Measurement
The Unit Base (UB) SHALL be StudCraft's universal measurement, equal to a volume measuring 4 studs wide, 3 studs deep and 13 plate layers tall. Thirteen plate layers SHALL equal exactly 4 standard bricks and one plate, and the height SHALL be measured from the underside of the base an infantry model stands on, which is part of the volume rather than the floor beneath it. That base SHALL be one physical base measuring 4 × 3 studs and one plate thick — the Unit Base read horizontally. Every distance, Deployment Volume, and vehicle or infantry footprint SHALL be expressed using this unit. Wherever a rule asks whether something physically fits, the volume that must fit SHALL be the Unit Base — one for a minifigure, its own volume in Unit Bases for a vehicle — and never the loose model.

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

### Requirement: Unit Base Projections
A rule SHALL read whichever projection of the Unit Base volume it requires: the horizontal projection (4 × 3 studs) for distances, movement, deployment floors and footprints; the volume itself for transport capacity, interior space, and the Deployment Volume a model must be placed inside; and the vertical projection across the front (4 studs × 13 plate layers) for whether something passes through an opening. A projection SHALL supply a measured value only. A projection SHALL NOT replace a physical check: Line of Sight and Cover SHALL be resolved against the physical model on the table, never against a Unit Base silhouette, and an army's legality SHALL be resolved by placing its models inside the agreed Deployment Volume rather than by summing a cost.

#### Scenario: Deployment reads the horizontal projection
- **WHEN** the floor space a vehicle occupies is read
- **THEN** it is the horizontal projection of the Unit Bases its footprint covers, and its height is read against the ceiling instead of adding to that floor space

#### Scenario: An opening is measured against the vertical projection
- **WHEN** an access opening is checked against an infantry model
- **THEN** the clear opening must measure at least 4 studs wide and 13 plate layers high

#### Scenario: Line of Sight is not traced against a projection
- **WHEN** visibility between an attacker and a target is resolved
- **THEN** it is resolved against the physical models on the table, and the Unit Base volume or any of its projections plays no part

#### Scenario: The agreed ceiling reads the volume
- **WHEN** a model is checked against the height agreed for the Deployment Volume
- **THEN** the reading is the volume itself rather than a projection of it, and the model's own height is measured from the surface it rests on to the top of its Gameplay Geometry

#### Scenario: An army is legal when its models can all be placed at once
- **WHEN** a player's whole force is checked against the agreed Deployment Volume
- **THEN** it is legal exactly when every model can be physically placed inside that volume at the same time without overlapping another, and no separate arithmetic on footprint totals is performed

### Requirement: Cargo Divides a Unit Base
Cargo SHALL be permitted to share one Unit Base, each object occupying a slice measuring 4 × 3 studs by its own height, with the slices sharing a Unit Base totalling no more than the Unit Base's height. An object narrower than 4 × 3 studs SHALL still occupy a whole slice of its own height, and an object whose footprint covers more than one Unit Base SHALL occupy a slice of its own height in each Unit Base it covers. Infantry SHALL never share a Unit Base.

#### Scenario: Three short crates share one Unit Base
- **WHEN** three crates of 4 plate layers each are loaded
- **THEN** they share one Unit Base, their slices totalling less than its height

#### Scenario: A crate never shares with a minifigure
- **WHEN** a 4-plate-layer crate and an infantry model are loaded
- **THEN** they occupy two Unit Bases, because the infantry model occupies a whole one on its own

#### Scenario: A narrow object still costs a whole slice
- **WHEN** an object narrower than 4 × 3 studs is loaded
- **THEN** it occupies a slice 4 × 3 studs wide by its own height

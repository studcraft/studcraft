# unit-base Specification Delta

`a-deployment-volume-is-floor-and-ceiling` (#129) is applied to `docs/` and not
yet archived, so it carries an unarchived `MODIFIED` delta against this same
requirement. **This change is the later one and carries the authoritative
delta** (`system/workflow.md`, "When several changes modified the same
requirement"). #129's delta is superseded and moves to `specs-superseded/` in
its own directory, in its own pull request — `tasks.md`, B11.

The requirement below is written against `openspec/specs/unit-base/spec.md` as
it stands today, which is the pre-#129 text.

## MODIFIED Requirements

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

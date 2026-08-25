# infantry-movement Specification

## Purpose
TBD - created by archiving change fix-infantry. Update Purpose after archive.

## Requirements

### Requirement: Infantry Distances Are Counted In Unit Bases
Infantry movement SHALL be stated as a whole number of Unit Bases (`02-core-rules.md`, CORE-001), and each movement rule SHALL name which axis of the Unit Base it reads. Forward and backward movement SHALL read the Unit Base's 3-stud depth and SHALL be limited to 4 UB. Sideways movement SHALL read its 4-stud width and SHALL be limited to 3 UB. A partial Unit Base SHALL NOT be moved, and a unit MAY move any whole number of Unit Bases up to its limit or stay where it is.

#### Scenario: Forward movement is four Unit Bases of depth
- **WHEN** an infantry model moves forward
- **THEN** it may move 1, 2, 3 or 4 Unit Bases read across the base's 3-stud depth, which is at most 12 studs, and no partial Unit Base

#### Scenario: Side movement is three Unit Bases of width
- **WHEN** an infantry model moves sideways
- **THEN** it may move 1, 2 or 3 Unit Bases read across the base's 4-stud width, which is at most 12 studs, and no partial Unit Base

#### Scenario: The two limits are the same distance
- **WHEN** the forward limit and the side limit are compared
- **THEN** both measure 12 studs, because each counts a different axis of the same Unit Base, and the smaller count is not the shorter move

#### Scenario: Backward movement reads the forward axis
- **WHEN** an infantry model moves backward
- **THEN** it moves up to 4 Unit Bases across the base's 3-stud depth, keeps its facing, and costs the 1 Action Point a forward move costs

### Requirement: A Movement Action Is Measured On Its Own
Each infantry movement action SHALL cost 1 Action Point (`02-core-rules.md`, CORE-006), SHALL travel in a single direction, and SHALL be measured independently of every other movement action in the same activation. Distance SHALL be measured from the face of the base that leads in the direction of travel. Two movement actions SHALL NOT be combined into one longer move, and an off-axis position SHALL be reached by combining a forward or backward action with a side action rather than by moving diagonally (`07-movement.md`, MOVE-007).

#### Scenario: Two Action Points are two moves
- **WHEN** an infantry model spends two Action Points moving forward
- **THEN** it makes two separate moves of up to 4 UB each, and not one move of 8 UB

#### Scenario: Distance is measured from the leading face
- **WHEN** an infantry move is measured
- **THEN** it is measured from the face of the base leading the direction of travel — the front face forward, the rear face backward, the corresponding side face sideways — and never from wherever the model is widest

#### Scenario: An off-axis position costs two actions
- **WHEN** an infantry model must reach a position that is neither straight ahead nor straight to the side
- **THEN** it spends one movement action forward or backward and a second sideways, each costing 1 Action Point

### Requirement: Climbing Is Charged For Each Obstacle Crossed
An obstacle of 4 to 6 plate layers SHALL cost 1 additional Action Point for each such obstacle a movement action crosses, charged on top of that action's own Action Point. A climb SHALL NOT increase the distance the moving unit may travel: the whole move SHALL count against the unit's normal limit. An obstacle of 3 plate layers or fewer SHALL cost nothing additional. A stepped surface SHALL be climbed one step at a time, each step read as an obstacle in its own right, and a step the unit cannot climb SHALL stop the climb at that step rather than making the whole surface impassable. What a unit may do with an obstacle of 7 or more plate layers is stated by `17-infantry.md` (INF-008) and is not restated here.

#### Scenario: One obstacle costs two Action Points
- **WHEN** a movement action crosses a single obstacle of 4 to 6 plate layers
- **THEN** the move costs 2 Action Points in total — 1 for the movement action and 1 for the climb

#### Scenario: A two-step staircase is charged twice
- **WHEN** a movement action climbs two steps of 4 to 6 plate layers each
- **THEN** it costs 3 Action Points, because two obstacles were crossed rather than one

#### Scenario: A step too tall stops the climb where it is
- **WHEN** a stepped surface's third step measures 7 or more plate layers
- **THEN** the climb stops below that step, and the two steps beneath it were still climbable

#### Scenario: A climb does not extend the move
- **WHEN** a movement action climbs an obstacle
- **THEN** the distance travelled up counts against the unit's normal limit of 4 UB, or against a Wounded model's shorter limit

### Requirement: A Wounded Infantry Model Moves At Most Two Unit Bases
A Wounded infantry model (`16-damage-system.md`, DMG-002) SHALL move at most 2 UB in whichever direction it travels, each direction reading its own axis of the Unit Base. Nothing else about the move SHALL change: it SHALL still cost 1 Action Point, still travel in a single direction, and still charge a climb the additional Action Point that climb costs. The limit SHALL be counted in whole Unit Bases rather than taken as a fraction of the normal distance.

#### Scenario: A Wounded model moves six studs forward
- **WHEN** a Wounded infantry model moves forward or backward
- **THEN** it moves at most 2 Unit Bases of depth, which is 6 studs

#### Scenario: A Wounded model moves eight studs sideways
- **WHEN** a Wounded infantry model moves sideways
- **THEN** it moves at most 2 Unit Bases of width, which is 8 studs

#### Scenario: The Wounded limit is a count, not a fraction
- **WHEN** the Wounded limit is derived
- **THEN** it is two whole Unit Bases, because half of a 3 UB side move is not a whole Unit Base

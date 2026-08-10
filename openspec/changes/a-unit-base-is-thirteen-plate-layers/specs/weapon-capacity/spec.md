## MODIFIED Requirements

### Requirement: Platform Length Definition
Platform Length SHALL be the largest horizontal dimension of the platform's Unit Base or vehicle bounding box. The Unit Base's height SHALL NOT be a candidate for Platform Length.

#### Scenario: Platform length from bounding box
- **WHEN** a vehicle platform has a base of 8×9
- **THEN** its Platform Length is 9

#### Scenario: Infantry Platform Length ignores the Unit Base's height
- **WHEN** an infantry platform of one Unit Base is measured
- **THEN** its Platform Length is 4 studs, and the Unit Base's height is not considered

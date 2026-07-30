## MODIFIED Requirements

### Requirement: Component State Progression
Every component SHALL progress through exactly three states: `Operational`, `Wounded`, and `Dead`. Every component in the game SHALL use this same progression, with no exceptions per component type.

#### Scenario: Operational component functions normally
- **WHEN** a component is in the `Operational` state
- **THEN** it functions normally

#### Scenario: Wounded component still functions
- **WHEN** a component is in the `Wounded` state
- **THEN** it continues to function normally, and a subsequent successful damaging effect will advance it to `Dead`

#### Scenario: Dead component is removed
- **WHEN** a component reaches the `Dead` state
- **THEN** it is immediately and physically removed from the model; no dead component remains on the battlefield

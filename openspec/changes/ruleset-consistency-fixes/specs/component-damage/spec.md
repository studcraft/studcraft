## MODIFIED Requirements

### Requirement: Component Targeting
Every attack SHALL target one visible component, never an entire unit. A vehicle or building SHALL be represented as a collection of independent components, each resolving Impacts on its own.

#### Scenario: Attack targets a component
- **WHEN** an attacker declares an attack against a vehicle
- **THEN** the attack is assigned to one visible component of that vehicle (e.g. a wheel, a turret, a pilot), never to the vehicle as a whole

#### Scenario: Vehicle has no unit-level health
- **WHEN** a vehicle's component is destroyed
- **THEN** only that component is affected; the vehicle itself does not possess or lose any unit-level health value

### Requirement: Internal Components
A component SHALL be able to protect another component positioned behind it. An Impact SHALL NOT affect a protected component until the protecting component has been penetrated or destroyed.

#### Scenario: Protected component is unaffected while cover exists
- **WHEN** a component (e.g. Armor) protects another component (e.g. Pilot) positioned behind it, and an Impact has not yet penetrated or destroyed the protecting component
- **THEN** the protected component is not affected by that Impact

#### Scenario: Protected component becomes exposed after penetration
- **WHEN** the protecting component has been penetrated or destroyed
- **THEN** the Impact may continue toward the previously protected component

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

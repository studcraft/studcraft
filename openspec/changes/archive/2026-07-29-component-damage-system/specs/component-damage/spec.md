## ADDED Requirements

### Requirement: Component Targeting
Every attack SHALL target one visible component, never an entire unit. A vehicle or building SHALL be represented as a collection of independent components, each resolving Impacts on its own.

#### Scenario: Attack targets a component
- **WHEN** an attacker declares an attack against a vehicle
- **THEN** the attack is assigned to one visible component of that vehicle (e.g. a wheel, a turret, an engine), never to the vehicle as a whole

#### Scenario: Vehicle has no unit-level health
- **WHEN** a vehicle's component is destroyed
- **THEN** only that component is affected; the vehicle itself does not possess or lose any unit-level health value

### Requirement: Components Have No Hit Points
Components SHALL NOT possess Hit Points, Armor Values, or any hidden numeric health statistic. A component's structural integrity SHALL be represented only by the Component State (see Component State Progression).

#### Scenario: No hidden health value exists
- **WHEN** a player inspects any component
- **THEN** no hidden Hit Point or health value is associated with it — only its current Component State and its Resistance, both derivable from the model

### Requirement: Geometry Defines Resistance
A component's Resistance SHALL be the smallest structural cross-section, measured in LEGO bricks or plates, that an Impact must cross in its direction of travel. Resistance SHALL NOT be assigned as an arbitrary statistic.

#### Scenario: Resistance read from a single-brick cross-section
- **WHEN** a component is built such that an Impact crosses exactly 1 brick in its direction of travel
- **THEN** that component's Resistance is 1

#### Scenario: Resistance read from a multi-plate cross-section
- **WHEN** a component is built from 4 stacked plates such that an Impact must cross all 4 in its direction of travel
- **THEN** that component's Resistance is 4

#### Scenario: Visually similar components may have different Resistance
- **WHEN** two components occupy similar external dimensions but are built with different internal construction (e.g. one from bricks, one from stacked plates)
- **THEN** their Resistance values may differ, according to their actual construction

### Requirement: Component State Progression
Every component SHALL progress through exactly three states: `OK`, `TOUCHED`, and `DESTROYED`. Every component in the game SHALL use this same progression, with no exceptions per component type.

#### Scenario: OK component functions normally
- **WHEN** a component is in the `OK` state
- **THEN** it functions normally

#### Scenario: TOUCHED component still functions
- **WHEN** a component is in the `TOUCHED` state
- **THEN** it continues to function normally, and a subsequent successful damaging effect will advance it to `DESTROYED`

#### Scenario: DESTROYED component is removed
- **WHEN** a component reaches the `DESTROYED` state
- **THEN** it is immediately and physically removed from the model; no destroyed component remains on the battlefield

### Requirement: Universal Destruction
Destruction SHALL mean exactly the same thing for every component: physical removal. No component type SHALL have a special-cased destruction rule.

#### Scenario: Destroying any component removes it
- **WHEN** any component (wheel, cannon, shield, door, minifig, or other) is destroyed
- **THEN** that component is removed from the model, using the same rule regardless of component type

### Requirement: Internal Components
A component SHALL be able to protect another component positioned behind it. An Impact SHALL NOT affect a protected component until the protecting component has been penetrated or destroyed.

#### Scenario: Protected component is unaffected while cover exists
- **WHEN** a component (e.g. Armor) protects another component (e.g. Engine) positioned behind it, and an Impact has not yet penetrated or destroyed the protecting component
- **THEN** the protected component is not affected by that Impact

#### Scenario: Protected component becomes exposed after penetration
- **WHEN** the protecting component has been penetrated or destroyed
- **THEN** the Impact may continue toward the previously protected component

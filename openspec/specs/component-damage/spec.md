# component-damage Specification

## Purpose
TBD - created by archiving change component-damage-system. Update Purpose after archive.
## Requirements
### Requirement: Component Targeting
Every attack SHALL target one visible component, never an entire unit. A vehicle or building SHALL be represented as a collection of independent components, each resolving Impacts on its own.

#### Scenario: Attack targets a component
- **WHEN** an attacker declares an attack against a vehicle
- **THEN** the attack is assigned to one visible component of that vehicle (e.g. a wheel, a turret, a pilot), never to the vehicle as a whole

#### Scenario: Vehicle has no unit-level health
- **WHEN** a vehicle's component is destroyed
- **THEN** only that component is affected; the vehicle itself does not possess or lose any unit-level health value

### Requirement: Components Have No Hit Points
Components SHALL NOT possess Hit Points, Armor Values, or any hidden numeric health statistic. A component's structural integrity SHALL be represented only by the Component State (see Component State Progression).

#### Scenario: No hidden health value exists
- **WHEN** a player inspects any component
- **THEN** no hidden Hit Point or health value is associated with it — only its current Component State and its Resistance, both derivable from the model

### Requirement: Geometry Defines Resistance
A component's Resistance SHALL be the smallest structural cross-section, measured in plate layers, that an Impact must cross in its direction of travel. Resistance SHALL NOT be assigned as an arbitrary statistic.

The conversion SHALL be stated once and applied to every component without exception: a plate counts as 1, a brick counts as 3, and any other LEGO element counts as the plate-equivalent of its own thickness in the direction of travel. No component type SHALL be exempt from this measurement, and no component type SHALL be named as a special case — a moulded element is measured by the same conversion as a built one.

Only material the Impact actually crosses SHALL contribute to Resistance. Empty internal space SHALL contribute nothing, and a component SHALL be assumed hollow unless it is physically built solid.

Where an Impact would cross more than one wall of an enclosed structure, those walls SHALL be treated as separate components, each with its own Resistance, resolved in sequence by Penetration. Their thicknesses SHALL NOT be summed into a single Resistance value.

Because Impact Strength is expressed in the same unit (`10-weapons.md`, WPN-021), the Geometry Check SHALL compare two counts of plate layers rather than two different units.

#### Scenario: Resistance read from a single-brick cross-section
- **WHEN** a component is built such that an Impact crosses exactly 1 brick in its direction of travel
- **THEN** that component's Resistance is 3, because a brick counts as 3 plate layers

#### Scenario: Resistance read from a single-plate cross-section
- **WHEN** a component is built such that an Impact crosses exactly 1 plate layer in its direction of travel
- **THEN** that component's Resistance is 1

#### Scenario: Resistance read from a multi-plate cross-section
- **WHEN** a component is built from 4 stacked plates such that an Impact must cross all 4 in its direction of travel
- **THEN** that component's Resistance is 4

#### Scenario: Resistance read from a multi-brick cross-section
- **WHEN** a component is built two bricks thick in its direction of travel
- **THEN** that component's Resistance is 6

#### Scenario: Visually similar components may have different Resistance
- **WHEN** two components occupy similar external dimensions but are built with different internal construction (e.g. one from a single brick, one from four stacked plates)
- **THEN** their Resistance values may differ according to their actual construction (3 vs. 4) — the count of physical layers, not the external silhouette, is what matters

#### Scenario: Empty interior contributes no Resistance
- **WHEN** a component encloses empty space behind its structural wall
- **THEN** only the wall's own plate-layer count is its Resistance, and the empty space adds nothing

#### Scenario: Opposing walls of a hollow structure are not summed
- **WHEN** an Impact strikes a hollow structure whose front and rear walls are each one brick thick
- **THEN** the front wall has Resistance 3 and the rear wall has Resistance 3 as a separate component, resolved in sequence by Penetration — the structure does not have a single Resistance of 6

#### Scenario: A moulded element is measured, not exempted
- **WHEN** a component is a single moulded LEGO element rather than a built assembly (for example a minifig torso, a windscreen, a wheel, or an accessory shield)
- **THEN** its Resistance is the plate-equivalent of its own thickness in the direction of travel, by the same conversion as any built component — a minifig torso is roughly one brick of material and therefore has Resistance 3

#### Scenario: No component carries a fixed or baseline Resistance
- **WHEN** any component's Resistance is determined
- **THEN** it is read from the model by the stated conversion, and no component type has a baseline, exempt, or material-derived value

### Requirement: Component State Progression
Every component SHALL progress through exactly three states: `Operational`, `Wounded`, and `Dead`. Every component in the game SHALL use this same progression, with no exceptions per component type. A `Wounded` component SHALL continue to function, and SHALL function worse only where the capability it provides is one of a closed list: the movement of a `Wounded` infantry model, the movement of a vehicle whose Pilot is `Wounded`, and how each Attack Die is read when the component providing the attack is `Wounded` — the weapon, or the attacker itself in an unarmed attack. What a `Wounded` component loses SHALL be set by the capability that component provides and never by the material it represents. No other property of a `Wounded` component SHALL change — Resistance, Impact Strength, the Damage Roll, Unit Base occupancy, footprint, transport capacity and Action Point costs SHALL all be read exactly as they are read for an `Operational` component.

#### Scenario: Operational component functions normally
- **WHEN** a component is in the `Operational` state
- **THEN** it functions normally

#### Scenario: Wounded component still functions
- **WHEN** a component is in the `Wounded` state
- **THEN** it still functions, with the capability it provides degraded, and a subsequent successful damaging effect will advance it to `Dead`

#### Scenario: Wounded changes only the capability the component provides
- **WHEN** a `Wounded` component is measured or resolved for anything other than the capability it provides
- **THEN** its Resistance, Impact Strength, Damage Roll, Unit Base occupancy, footprint, transport capacity and Action Point costs are exactly those of an `Operational` component

#### Scenario: Dead component is removed
- **WHEN** a component reaches the `Dead` state
- **THEN** it is immediately and physically removed from the model; no dead component remains on the battlefield

### Requirement: Universal Destruction
Destruction SHALL mean exactly the same thing for every component: physical removal. No component type SHALL have a special-cased destruction rule.

#### Scenario: Destroying any component removes it
- **WHEN** any component (wheel, cannon, shield, door, minifig, or other) is destroyed
- **THEN** that component is removed from the model, using the same rule regardless of component type

### Requirement: Internal Components
A component SHALL be able to protect another component positioned behind it. An Impact SHALL NOT affect a protected component until the protecting component has been penetrated or destroyed.

#### Scenario: Protected component is unaffected while cover exists
- **WHEN** a component (e.g. Armor) protects another component (e.g. Pilot) positioned behind it, and an Impact has not yet penetrated or destroyed the protecting component
- **THEN** the protected component is not affected by that Impact

#### Scenario: Protected component becomes exposed after penetration
- **WHEN** the protecting component has been penetrated or destroyed
- **THEN** the Impact may continue toward the previously protected component


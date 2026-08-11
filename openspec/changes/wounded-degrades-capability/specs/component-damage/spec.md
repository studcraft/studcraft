## MODIFIED Requirements

### Requirement: Component State Progression
Every component SHALL progress through exactly three states: `Operational`, `Wounded`, and `Dead`. Every component in the game SHALL use this same progression, with no exceptions per component type. A `Wounded` component SHALL continue to function with the capability it provides degraded, and those degradations SHALL form a closed list: the movement of a `Wounded` infantry model, the movement of a vehicle whose Pilot is `Wounded`, and how each Attack Die is read when the component providing the attack is `Wounded` — the weapon, or the attacker itself in an unarmed attack. What a `Wounded` component loses SHALL be set by the capability that component provides and never by the material it represents. No other property of a `Wounded` component SHALL change — Resistance, Impact Strength, the Damage Roll, Unit Base occupancy, footprint, transport capacity and Action Point costs SHALL all be read exactly as they are read for an `Operational` component.

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

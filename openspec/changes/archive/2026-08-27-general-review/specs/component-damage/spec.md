# component-damage Specification Delta

`DMG-002` and `DMG-005` were two rules saying one thing: components carry no
health value, and the three states are what they carry instead. They are now one
rule, `DMG-002`. **Neither requirement below loses anything it stated**; both
are stated by the same rule.

The second requirement also names the Damage Roll again. The compressed text
lists what a `Wounded` component keeps and omits it, which reads as an opening
where the living spec has none — `tasks.md`, B6.

## MODIFIED Requirements

### Requirement: Components Have No Hit Points
Components SHALL NOT possess Hit Points, Armor Values, or any hidden numeric health statistic. A component's structural integrity SHALL be represented only by the Component State. This SHALL be stated by the same rule that states Component State Progression, since the absence of a health value and the presence of the three states are one statement read from two sides.

#### Scenario: No hidden health value exists
- **WHEN** a player inspects any component
- **THEN** no hidden Hit Point or health value is associated with it — only its current Component State and its Resistance, both derivable from the model

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

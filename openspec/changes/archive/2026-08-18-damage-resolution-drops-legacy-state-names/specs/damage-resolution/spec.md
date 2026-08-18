## MODIFIED Requirements

### Requirement: Damage Roll
When an Impact passes the Geometry Check, the defender SHALL roll one D6. A result of 4, 5, or 6 SHALL leave the component's state unchanged. A result of 1, 2, or 3 SHALL advance the component's state by exactly one step (`Operational` to `Wounded`, or `Wounded` to `Dead`).

#### Scenario: Successful damage roll leaves the component unchanged
- **WHEN** a Damage Roll results in 4, 5, or 6
- **THEN** the target component's state does not change

#### Scenario: Failed damage roll advances the component's state
- **WHEN** a Damage Roll results in 1, 2, or 3
- **THEN** the target component's state advances by exactly one step

### Requirement: Repairs
Repairing a component SHALL consume Action Points and SHALL restore exactly one state, from `Wounded` to `Operational`. A `Dead` component SHALL NOT be repairable.

#### Scenario: Repairing a touched component
- **WHEN** a player spends the required Action Points to repair a component in the `Wounded` state
- **THEN** that component returns to the `Operational` state

#### Scenario: Destroyed components cannot be repaired
- **WHEN** a component is in the `Dead` state
- **THEN** it cannot be repaired, since it has already been removed from the model

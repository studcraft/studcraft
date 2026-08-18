## MODIFIED Requirements

### Requirement: Damage Roll
When an Impact passes the Geometry Check, the defender — or the attacker, where `11-combat.md` (CBT-008) directs — SHALL roll one D6. A result of 4, 5, or 6 SHALL leave the component's state unchanged. A result of 1, 2, or 3 SHALL advance the component's state by exactly one step (`Operational` to `Wounded`, or `Wounded` to `Dead`).

#### Scenario: Successful damage roll leaves the component unchanged
- **WHEN** a Damage Roll results in 4, 5, or 6
- **THEN** the target component's state does not change

#### Scenario: Failed damage roll advances the component's state
- **WHEN** a Damage Roll results in 1, 2, or 3
- **THEN** the target component's state advances by exactly one step

#### Scenario: The attacker rolls when the target component has no controlling player
- **WHEN** a Damage Roll is required for a target component that has no controlling player
- **THEN** the attacking player makes that Damage Roll instead of a defender

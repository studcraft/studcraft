## MODIFIED Requirements

### Requirement: Select Target Component
Every valid Impact SHALL be assigned to exactly one visible component. Impacts SHALL NOT be assigned to an entire vehicle or building. A player MAY only select a component they can physically see.

#### Scenario: Impact assigned to a single visible component
- **WHEN** a valid Impact is resolved against a vehicle or building
- **THEN** it is assigned to exactly one visible component of that target, never to the target as a whole

#### Scenario: Hidden components cannot be selected
- **WHEN** a component is not physically visible to the attacker
- **THEN** that component cannot be selected as the target of an Impact

### Requirement: Composite Vehicle Targeting
A player SHALL be able to choose which visible component of a composite target (vehicle or building) to attack. The consequence of destroying one component SHALL be independent of every other component: destroying one component SHALL NOT change the state of any other component. When a single attack generates multiple valid Impacts, each Impact MAY be assigned to a different visible component of the same target.

#### Scenario: Player chooses which component to attack
- **WHEN** a composite target has multiple visible components (e.g. cannon, driver, wheels)
- **THEN** the attacking player may choose which one to target

#### Scenario: Destroying one component does not affect another
- **WHEN** one component of a composite target is destroyed
- **THEN** every other component of that target keeps its own current state, unaffected by that destruction

#### Scenario: Multiple impacts split across different components in one attack
- **WHEN** a single attack generates multiple valid Impacts against a composite target
- **THEN** each Impact may be assigned to a different visible component of that target, and each assigned component resolves only the Impacts it received

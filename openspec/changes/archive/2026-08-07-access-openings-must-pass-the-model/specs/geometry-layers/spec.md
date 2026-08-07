## MODIFIED Requirements

### Requirement: Visual Geometry Still Applies to Physical Checks
Visual Geometry SHALL be considered, together with Gameplay Geometry, whenever a rule is a direct physical check against the model rather than a measured value. This applies at minimum to Line of Sight, Cover, and whether an access point's opening passes the models that use it.

#### Scenario: Decoration blocks line of sight
- **WHEN** a decorative element physically obstructs the view between an attacker and a target
- **THEN** the target is not visible, exactly as if the obstruction were part of Gameplay Geometry

#### Scenario: Decoration can complete concealment
- **WHEN** a decorative element physically hides a component completely from an attacker's viewpoint
- **THEN** that component cannot be selected as a target, exactly as if the obstruction were part of Gameplay Geometry — Cover is binary and grants no bonus for partial concealment

#### Scenario: Decoration narrows an access opening
- **WHEN** decorative elements around a door, hatch or portal reduce the opening so that a model which would otherwise fit can no longer be passed through it
- **THEN** that access point is decorative for that model and has no gameplay effect, exactly as if the obstruction were part of Gameplay Geometry

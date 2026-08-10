# action-economy Specification

## Purpose
TBD - created by archiving change consolidate-core-measurements. Update Purpose after archive.
## Requirements
### Requirement: Universal Action Points
Every unit SHALL receive exactly 3 Action Points (AP) when activated, regardless of its type or construction. No unit SHALL gain additional AP through its profile.

#### Scenario: Every unit receives 3 AP
- **WHEN** any unit (infantry, vehicle, walker, hovercraft, or future unit type) is activated
- **THEN** it receives exactly 3 Action Points

#### Scenario: No unit gains extra AP
- **WHEN** a unit's construction or type is considered
- **THEN** it does not grant that unit any Action Points beyond the universal 3

### Requirement: Action Cost Does Not Scale With Size
An action's Action Point cost SHALL NOT scale with the size of the unit performing it — its footprint, its height, or the number of Unit Bases it occupies — nor with the size of an element that action operates. Where more than one Action Point is spent, the reason SHALL be stated in the rule that spends it and SHALL NOT be size. A measurement MAY decide which rule applies to an action; it SHALL NOT decide what that action costs.

#### Scenario: Infantry embarks for one Action Point
- **WHEN** an infantry model occupying one Unit Base embarks
- **THEN** it spends 1 Action Point

#### Scenario: A larger unit embarks for the same cost
- **WHEN** a unit occupying four Unit Bases embarks
- **THEN** it spends 1 Action Point

#### Scenario: Disembarking costs the same as embarking
- **WHEN** an embarked unit disembarks
- **THEN** it spends 1 Action Point, whatever it occupies

#### Scenario: A larger element costs no more to operate
- **WHEN** a small hatch and a large gate are each opened
- **THEN** each costs the same number of Action Points


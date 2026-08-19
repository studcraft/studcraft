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

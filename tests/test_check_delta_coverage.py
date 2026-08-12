"""A `## MODIFIED Requirements` block replaces the whole requirement, so a
scenario it leaves out is deleted at archive time. This is the parsing that
decides whether one is missing.
"""

from __future__ import annotations

import check_delta_coverage as coverage

DELTA = """## ADDED Requirements

### Requirement: Component Targeting

#### Scenario: A visible component is chosen

## MODIFIED Requirements

### Requirement: Damage Roll

#### Scenario: A die meets the Geometry Check

#### Scenario: A die falls short

### Requirement: Repairs

#### Scenario: A component is rebuilt

## REMOVED Requirements

### Requirement: Material Table

#### Scenario: Plastic resists nothing
"""


class TestReadingADelta:
    def test_only_modified_requirements_are_returned(self):
        blocks = coverage.modified_blocks(DELTA)
        assert sorted(blocks) == ["Damage Roll", "Repairs"]

    def test_each_requirement_carries_its_own_scenarios(self):
        blocks = coverage.modified_blocks(DELTA)
        assert blocks["Damage Roll"] == {
            "A die meets the Geometry Check",
            "A die falls short",
        }
        assert blocks["Repairs"] == {"A component is rebuilt"}

    def test_two_modified_blocks_naming_one_requirement_are_merged(self):
        # Assignment would drop the first block's scenarios, which is the silent
        # deletion this whole script exists to catch.
        delta = (
            "## MODIFIED Requirements\n\n"
            "### Requirement: Damage Roll\n\n"
            "#### Scenario: A die meets the Geometry Check\n\n"
            "## MODIFIED Requirements\n\n"
            "### Requirement: Damage Roll\n\n"
            "#### Scenario: A die falls short\n"
        )
        assert coverage.modified_blocks(delta)["Damage Roll"] == {
            "A die meets the Geometry Check",
            "A die falls short",
        }

    def test_a_delta_with_no_modified_section_is_empty(self):
        assert coverage.modified_blocks("## ADDED Requirements\n\n### Requirement: X\n") == {}


class TestReadingALivingSpec:
    def test_every_requirement_and_scenario_is_found(self):
        spec = (
            "# damage-resolution\n\n"
            "### Requirement: Damage Roll\n\n"
            "#### Scenario: A die meets the Geometry Check\n\n"
            "#### Scenario: A die falls short\n\n"
            "### Requirement: Repairs\n\n"
            "#### Scenario: A component is rebuilt\n"
        )
        living = coverage.living_requirements(spec)
        assert sorted(living) == ["Damage Roll", "Repairs"]
        assert len(living["Damage Roll"]) == 2

    def test_a_scenario_the_delta_omits_is_the_difference(self):
        living = coverage.living_requirements(
            "### Requirement: Damage Roll\n\n"
            "#### Scenario: A die meets the Geometry Check\n\n"
            "#### Scenario: A die falls short\n"
        )
        delta = coverage.modified_blocks(
            "## MODIFIED Requirements\n\n"
            "### Requirement: Damage Roll\n\n"
            "#### Scenario: A die falls short\n"
        )
        missing = living["Damage Roll"] - delta["Damage Roll"]
        assert missing == {"A die meets the Geometry Check"}

"""`assets/IMAGES.md` parsed once, for the three scripts that read it.

The parsing moved here out of `lint_ruleset.py` when `insert_images.py` and
`build_index.py` became readers too — three parsers would have been three
answers to what an entry is. The first three cases below came with it.

What a row *means* is tested here; whether a row is *allowed* stays in
`tests/test_lint_ruleset.py`, which is where the checking stayed.
"""

from __future__ import annotations

import images_index

IMAGES = """# Image index

| Column | Meaning |
|---|---|
| Rule | the rule illustrated |

## docs/10-weapons.md

| Rule | File |
|---|---|
| WPN-020 | `assets/images/wpn-020-muzzle-placement.png` |
| Terrain (WPN-018 – WPN-019) | `assets/images/10-weapon-grid.png` |

## Not a document heading

| Rule | File |
|---|---|
| WPN-001 | `assets/images/wpn-001-ignored.png` |
"""


class TestParsing:
    def test_only_rows_under_a_document_heading_are_entries(self):
        assert [entry.path for entry in images_index.parse(IMAGES)] == [
            "assets/images/wpn-020-muzzle-placement.png",
            "assets/images/10-weapon-grid.png",
        ]

    def test_each_entry_carries_the_document_it_sits_under(self):
        assert {entry.doc for entry in images_index.parse(IMAGES)} == {"10-weapons.md"}

    def test_a_row_naming_no_file_is_still_returned(self):
        text = "## docs/10-weapons.md\n\n| Rule | File |\n|---|---|\n| WPN-020 | to be drawn |\n"
        (entry,) = images_index.parse(text)
        assert entry.path == ""

    def test_the_prose_columns_are_carried_when_they_are_there(self):
        text = (
            "## docs/10-weapons.md\n\n| Rule | File | Show | Why |\n|---|---|---|---|\n"
            "| WPN-020 | `assets/images/wpn-020-muzzle.png` | Four panels. | Spatial. |\n"
        )
        (entry,) = images_index.parse(text)
        assert (entry.must_show, entry.why) == ("Four panels.", "Spatial.")


class TestTheTwoKindsOfEntry:
    """A Rule cell is either exactly one ID or it is a heading, and the two take
    different filename prefixes. Everything downstream reads that distinction."""

    def test_a_cell_that_is_one_id_is_the_numbered_case(self):
        numbered, unnumbered = images_index.parse(IMAGES)
        assert numbered.is_numbered
        assert not unnumbered.is_numbered

    def test_the_numbered_case_anchors_on_its_rule(self):
        numbered, _ = images_index.parse(IMAGES)
        assert numbered.anchor == "WPN-020"
        assert numbered.expected_prefix == "wpn-020"

    def test_the_unnumbered_case_anchors_on_the_heading_without_its_range(self):
        _, unnumbered = images_index.parse(IMAGES)
        assert unnumbered.anchor == "Terrain"
        assert unnumbered.expected_prefix == "10"


class TestAltText:
    """Derived from the slug, not the rule's title: a rule may specify several
    images, and their titles would be identical."""

    def test_the_slug_is_the_filename_without_prefix_or_extension(self):
        numbered, _ = images_index.parse(IMAGES)
        assert numbered.slug == "muzzle-placement"

    def test_two_images_on_one_rule_get_different_alt_text(self):
        text = (
            "## docs/10-weapons.md\n\n| Rule | File |\n|---|---|\n"
            "| WPN-020 | `assets/images/wpn-020-muzzle-placement.png` |\n"
            "| WPN-020 | `assets/images/wpn-020-front-footprint.png` |\n"
        )
        first, second = images_index.parse(text)
        assert first.alt == "WPN-020 — muzzle placement"
        assert second.alt == "WPN-020 — front footprint"

    def test_a_filename_without_its_entrys_prefix_yields_no_slug(self):
        text = (
            "## docs/10-weapons.md\n\n| Rule | File |\n|---|---|\n"
            "| WPN-020 | `assets/images/muzzle-placement.png` |\n"
        )
        (entry,) = images_index.parse(text)
        assert entry.slug == ""
        assert entry.alt == "WPN-020"

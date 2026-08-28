"""The one procedure that begins with a file gets named at the start of a session.

`.claude/hooks/session_orientation.py` reads `git status --short` and says what
it found. Everything it reports is recoverable by running the command; the line
that is not is the image one — a file under `assets/images/` is the start of a
procedure, and nothing else in a session says so, because a file appearing is
not an edit and not a prompt.

That line is the whole of what is pinned here. The hook lives outside
`scripts/`, so it is loaded by path rather than imported by name.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
HOOK = PROJECT_ROOT / ".claude" / "hooks" / "session_orientation.py"


def load():
    """The hook as a module. It is not on `pythonpath`, and should not be."""
    spec = importlib.util.spec_from_file_location("session_orientation", HOOK)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


orientation = load()


class TestUnplacedImages:
    def test_an_untracked_image_is_reported(self):
        status = "?? assets/images/cmp-018-clear-opening.png"
        assert orientation.unplaced_images(status) == ["cmp-018-clear-opening.png"]

    def test_a_replaced_image_is_reported_too(self):
        """A redraw is a placement read the same way: the file is uncommitted."""
        status = " M assets/images/core-001-unit-base-volume.png"
        assert orientation.unplaced_images(status) == ["core-001-unit-base-volume.png"]

    def test_the_directory_keeper_is_not_an_image(self):
        status = "?? assets/images/.gitkeep"
        assert orientation.unplaced_images(status) == []

    def test_changes_elsewhere_are_not_reported(self):
        status = " M docs/05-construction-components.md\n M assets/IMAGES.md"
        assert orientation.unplaced_images(status) == []

    def test_an_image_among_other_changes_is_still_found(self):
        """The real case: the placement branch is mid-flight and the tree is busy."""
        status = "\n".join((
            " M docs/05-construction-components.md",
            "?? assets/images/cmp-018-clear-opening.png",
            "?? openspec/changes/add-image-to-clear-opening-rule/",
        ))
        assert orientation.unplaced_images(status) == ["cmp-018-clear-opening.png"]

    def test_several_are_reported_in_order(self):
        status = "\n".join((
            "?? assets/images/veh-008-pivot.png",
            "?? assets/images/cmp-018-clear-opening.png",
        ))
        assert orientation.unplaced_images(status) == [
            "cmp-018-clear-opening.png",
            "veh-008-pivot.png",
        ]

    def test_a_clean_tree_reports_nothing(self):
        assert orientation.unplaced_images("") == []

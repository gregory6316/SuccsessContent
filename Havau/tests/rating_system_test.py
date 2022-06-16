"""Tests for rating system."""

from main import MainApp
from widgets.custom_widgets import StarButtonsContainer


def test_get_build_container():
    """Check that star buttons created correct."""
    MainApp()
    buttons_container = StarButtonsContainer(stars_count=7)
    for widget in buttons_container.children:
        assert 1 <= widget.value <= 7

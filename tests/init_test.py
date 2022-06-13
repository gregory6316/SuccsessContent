"""Tests for init card."""
from main import MainApp


def test_init_card():
    """Check if init works properly."""
    app = MainApp()
    assert not app.storage.inited()
    app.run()
    assert app.storage.inited()

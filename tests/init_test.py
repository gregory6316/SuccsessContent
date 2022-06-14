"""Tests for init card."""
import os
import shutil
import tempfile
from kivy.base import EventLoop
from kivy.tests.common import GraphicUnitTest

from main import MainApp

class MyTestCase(GraphicUnitTest):
    """Test with graphics."""

    @staticmethod
    def test_init_card():
        """Simple init test."""
        tmp_dict = tempfile.mkdtemp()

        path = os.path.join(tempfile.mkdtemp(), 'storage.dict')
        app = MainApp(path)
        assert not app.storage.inited()
        EventLoop.ensure_window()
        app.run()
        assert app.storage.inited()

        shutil.rmtree(tmp_dict)

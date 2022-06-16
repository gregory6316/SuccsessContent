"""Tests for init card."""
import os
import shutil
import tempfile
from kivy.base import EventLoop
from kivy.tests.common import GraphicUnitTest
from kivymd.uix.list import OneLineIconListItem

from main import MainApp, RateScreensManger


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

    @staticmethod
    def test_rate_screen_manager():
        """Simple menu test."""
        tmp_dict = tempfile.mkdtemp()

        path = os.path.join(tempfile.mkdtemp(), 'storage.dict')
        MainApp(path)
        rate_screen = RateScreensManger()
        screens_count = 4
        for widget in rate_screen.screen_manager.walk():
            if isinstance(widget, OneLineIconListItem):
                screens_count -= 1

        assert screens_count == 0

        shutil.rmtree(tmp_dict)

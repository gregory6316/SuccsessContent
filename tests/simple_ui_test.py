import os
import sys
import time
sys.path.insert(1, '..')
from main import MainApp
from widgets.mood_screen import MoodScreen
from widgets.mood_rating import MoodRating
from kivy.lang import Builder
import pytest

class TestLocale:
    def test_get_description(self):
        m_r = open("../widgets/mood_rating/description.kv", "r").read()
        m_s = open("../widgets/mood_screen/description.kv", "r").read()
        assert(m_r == MoodRating.get_descritpion())
        assert(m_s == MoodScreen.get_descritpion())

    def test_mood_rating(self):

        app = MainApp()
        Builder.load_string(MoodRating.get_descritpion())
        widget = MoodRating()
        assert(widget.children[1].text == 'Remove last rate')
        assert(widget.children[1].pos_hint == {'center_x': 0.5, 'center_y': 0.5})
        assert(widget.children[2].children[0].min == 0.0)
        assert(widget.children[2].children[0].value == 80)
        assert(widget.children[3].children[0].xlabel == 'Mood rate')


    def test_mood_screen(self):

        app = MainApp()
        Builder.load_string(MoodScreen.get_descritpion())
        widget = MoodScreen()
        assert(widget.children[0].children[0].text == '[u][size=24][b]Powered by[/b][/size][/u]\nSuccessContent')
        assert(widget.children[0].children[1].text == 'Rate us')
        assert(widget.children[0].children[2].text == 'Start!')
        assert(widget.children[0].children[3].text == 'Welcome to\n[b]}{avau![/b]')



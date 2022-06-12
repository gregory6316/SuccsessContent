"""Tests for UI."""
from kivy.lang import Builder
from main import MainApp
from widgets.mood_screen import RateScreen
from widgets.mood_rating import MoodRating


def test_get_description():
    """Test existence of of description.kv file."""
    for kv_path, module in [
        ("../widgets/mood_rating/description.kv", MoodRating),
        ("../widgets/mood_screen/description.kv", RateScreen)
    ]:
        with open(kv_path, encoding="utf-8") as kv_file:
            kv_content = kv_file.read()

        assert kv_content == module.get_descritpion()


def test_mood_rating():
    """Test MoodRating UI."""
    MainApp()
    Builder.load_string(MoodRating.get_descritpion())
    widget = MoodRating()
    assert widget.children[1].text == 'Remove last rate'
    assert widget.children[1].pos_hint == {'center_x': 0.5, 'center_y': 0.5}
    assert widget.children[2].children[0].min == 0.0
    assert widget.children[2].children[0].value == 80
    assert widget.children[3].children[0].xlabel == 'Mood rate'


def test_mood_screen():
    """Test RateScreen UI."""
    MainApp()
    Builder.load_string(RateScreen.get_descritpion())
    widget = RateScreen()
    assert widget.children[0].children[0].text == '[u][size=24][b]Powered by[/b][/size][/u]\nSuccessContent'
    assert widget.children[0].children[1].text == 'Rate us'
    assert widget.children[0].children[2].text == 'Start!'
    assert widget.children[0].children[3].text == 'Welcome to\n[b]}{avau![/b]'

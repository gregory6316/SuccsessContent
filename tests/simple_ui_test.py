"""Tests for UI."""
from kivy.lang import Builder
from main import MainApp
from widgets.mood_screen import RateScreen
from widgets.greeting_card import GreetingCard
from widgets.custom_widgets import CustomCard


def test_get_description():
    """Test existence of of description.kv file."""
    for kv_path, module in [
            ("widgets/greeting_card/description.kv", GreetingCard),
            ("widgets/mood_screen/description.kv", RateScreen),
            ("widgets/custom_widgets/description.kv", CustomCard)
    ]:
        with open(kv_path, encoding="utf-8") as kv_file:
            kv_content = kv_file.read()


        assert kv_content == module.get_descritpion()

def test_mood_screen():
    """Test RateScreen UI."""
    MainApp()
    Builder.load_string(RateScreen.get_descritpion())
    widget = RateScreen()
    assert widget.children[0].children[0].children[1].children[1].hint_text == 'Commentary'
    assert widget.children[0].children[0].children[2].children[1].text == 'Days in a Row'


def test_greeting_card():
    """Test Greeting card UI."""
    MainApp()
    Builder.load_string(GreetingCard.get_descritpion())
    widget = GreetingCard()
    assert widget.children[0].text == '[u][size=24][b]Powered by[/b][/size][/u]\nSuccessContent'
    assert widget.children[1].text == 'Rate us'
    assert widget.children[2].text == 'Start!'
    assert widget.children[3].text == 'Welcome to\n[b]}{avau![/b]'

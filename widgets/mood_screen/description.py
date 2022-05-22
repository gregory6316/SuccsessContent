"""Mood Screen."""

import pkgutil

from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from kivymd.uix.boxlayout import MDBoxLayout
from widgets.custom_widgets import CurrentDayCard, DaysInRowCard, RateHabit


class MoodScreen(Screen):
    """Container for Mood Screen content."""

    def __init__(self, **kwargs):
        """Init basics.

        Inits scrollable container for cards.
        Inits cards.
        Inits greeting card if the first run.
        """
        super().__init__(**kwargs)

        scrollview = ScrollView(
            do_scroll_y=True,
            do_scroll_x=False
        )

        cards_panel = MDBoxLayout(
            orientation="vertical",
            size_hint_y=None,
            padding=(0, 10, 0, 0),
            spacing=10
        )
        cards_panel.bind(minimum_height=cards_panel.setter("height"))

        current_day_card = CurrentDayCard(
            icon='emoticon-outline',
            msg='Have a nice day!',
            pos_hint={"center_x": 0.5}
        )

        days_in_row_card = DaysInRowCard(
            pos_hint={"center_x": 0.5}
        )

        cards_panel.add_widget(current_day_card)
        cards_panel.add_widget(days_in_row_card)
        cards_panel.add_widget(RateHabit(
            pos_hint={"center_x": 0.5}
        ))

        scrollview.add_widget(cards_panel)
        self.add_widget(scrollview)


    @staticmethod
    def get_descritpion() -> str:
        """Return kv description content."""
        return pkgutil.get_data(__name__, "description.kv").decode("utf-8")

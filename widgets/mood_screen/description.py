"""Rate Screen."""

import pkgutil

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from widgets.custom_widgets import CurrentDayCard, DaysInRowCard, RateHabit, Chart


class RateScreen(Screen):
    """Container for RateScreen content."""

    def __init__(self, **kwargs):
        """Init basics.

        Inits scrollable container for cards.
        Inits cards.
        Inits greeting card if the first run.
        """
        storage = MDApp.get_running_app().storage

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
            height=80
        )

        cards_panel.add_widget(current_day_card)
        cards_panel.add_widget(DaysInRowCard(storage, self.name))
        cards_panel.add_widget(RateHabit(storage, self.name))
        self.chart = Chart()
# storage,
# self.name,
# height = 400
# )
        cards_panel.add_widget(self.chart)

        scrollview.add_widget(cards_panel)
        self.add_widget(scrollview)


    @staticmethod
    def get_descritpion() -> str:
        """Return kv description content."""
        return pkgutil.get_data(__name__, "description.kv").decode("utf-8")

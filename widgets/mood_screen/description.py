"""
.. module:: mood_screen
   :synopsis:
       Rate Screen.

.. moduleauthor:: SuccsessContent <github.com/SuccsessContent>


"""
import locale
import gettext
import pkgutil

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from widgets.custom_widgets import CurrentDayCard, DaysInRowCard, RateHabit, Calendar, Chart



def setlocale(loc=None):
    """
    Function for setting locale.

    """
    if loc is None:
        locs = locale.getdefaultlocale()[0]
    else:
        locs = loc
    lc_loc = gettext.translation('mood_screen', localedir='locales', languages=[locs])
    lc_loc.install()
    return lc_loc.gettext

class RateScreen(Screen):
    """
    Container for RateScreen content.

    """

    def __init__(self, **kwargs):
        """
        Init basics.

        Inits scrollable container for cards.
        Inits cards.
        Inits greeting card if the first run.

        """
        self.storage = MDApp.get_running_app().storage

        super().__init__(**kwargs)
        _ = setlocale()
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
            msg=_('Have a nice day!'),
            height=80
        )

        cards_panel.add_widget(current_day_card)

        cards_panel.add_widget(DaysInRowCard(self.storage, self.name))
        cards_panel.add_widget(RateHabit(self.storage, self.name))
        self.chart = Chart(
            self.storage,
            self.name,
            height=200
        )
        cards_panel.add_widget(self.chart)
        cards_panel.add_widget(Calendar(self.storage, self.name))

        scrollview.add_widget(cards_panel)
        self.add_widget(scrollview)

    def update(self):
        """
        Update the cards statuses.

        """
        cards = self.children[0].children[0].children
        for card in cards:
            if card.need_update:
                card.update()

    @staticmethod
    def get_descritpion() -> str:
        """
        Return kv description content.

        """
        return pkgutil.get_data(__name__, "description.kv").decode("utf-8")

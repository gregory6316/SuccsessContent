"""Mood Screen."""

import pkgutil

from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.animation import Animation

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard

from widgets.custom_widgets import CurrentDayCard, DaysInRowCard
import locale
import gettext

"""
.. module:: mood_screen
   :synopsis: 
       Module for mood screen

.. moduleauthor:: SuccsessContent <github.com/SuccsessContent>


"""

def setlocale(loc=None):
    if loc is None:
        l = locale.getdefaultlocale()[0]
    else:
        l = loc
    lc = gettext.translation('mood_screen', localedir='locales', languages=[l])
    lc.install()
    return lc.gettext, lc.ngettext

class GreetingCard(MDCard):
    """

    **GreetingCard**

    Card with greetings message in first run of app.

    Code is in description.kv file.

    Contains:
        "Welcome to }{avau" message.
        "Start!" button: closes greetin card.
        "Rate us" button: allows user to rate the app.
        "Powered by" message.


    """

    def __init__(self, **kwargs):
        """

        **GreetingCard.__init__**

        Init greetings card.


        """
        super().__init__(**kwargs)
        print("TODO RateUs button")
        

class MoodScreen(Screen):
    """

    **MoodScreen**

    Container for Mood Screen content.


    """

    def __init__(self, **kwargs):
        """

        **MoodScreen.__init__**

        Init basics.

        Inits scrollable container for cards.
        Inits cards.
        Inits greeting card if the first run.


        """

        super().__init__(**kwargs)

        self.inited = False
        _, ngettext = setlocale()
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
            pos_hint={"center_x": 0.5}
        )

        days_in_row_card = DaysInRowCard(
            pos_hint={"center_x": 0.5}
        )

        cards_panel.add_widget(current_day_card)
        cards_panel.add_widget(days_in_row_card)

        scrollview.add_widget(cards_panel)
        self.add_widget(scrollview)

        if not self.inited:
            mdcard = GreetingCard(
                orientation="vertical",
                spacing=14,
                size_hint=[0.9, 0.7],
                pos_hint={"center_x": 0.5, "center_y": -0.5},
            )
            self.mdcard = mdcard
            self.add_widget(mdcard)

    @staticmethod
    def animate_open_card(widget):
        """

        **MoodScreen.animate_open_card**

        Animate greetins card's opening.

        Args:
        widget - greetings card.

        Returns:
        None.


        """
        animation = Animation(
            pos_hint={"center_y": 0.6}
        )
        animation.start(widget)

    def on_enter(self, *args):
        """

        **MoodScreen.on_enter**

        Start animation if screen is opened.


        """
        if not self.inited:
            self.animate_open_card(self.mdcard)

    def animate_close_card(self, widget):
        """

        **MoodScreen.animate_close_card**

        Animate greetins card's closing.

        Args:
        widget - greetings card

        Returns:
        None

        """
        animation = Animation(
            pos_hint={"center_y": -0.5}
        )
        animation.bind(on_complete=\
            lambda *x: self.remove_widget(widget))
        animation.start(widget)

    @staticmethod
    def get_descritpion() -> str:
        """

        **MoodScreen.get_descritpion**

        Return kv description content.

        """
        return pkgutil.get_data(__name__, "description.kv").decode("utf-8")

"""Main.

.. module:: main
   :synopsis:
       File with application entry point and intercomponents communication controller.

.. moduleauthor:: SuccsessContent <github.com/SuccsessContent>

"""

from functools import partial
import locale
import gettext
import os

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, OneLineIconListItem, IconLeftWidget
from widgets.custom_widgets import CustomCard
from widgets.mood_screen import RateScreen
from widgets.greeting_card import GreetingCard

from custom_storage import Storage


def _module_dir(rel_path):
    """Return path relative to current module dir."""
    return os.path.join(os.path.dirname(__file__), rel_path)


def setlocale(loc=None):
    """Set locale."""
    if loc :
        locs = loc
    else:
        locs = locale.getdefaultlocale()[0]
    lc_loc = gettext.translation('main', localedir=_module_dir('locales'), languages=[locs])
    lc_loc.install()
    return lc_loc.gettext


class RateScreensManger(MDNavigationLayout):
    """Main screen manager."""

    def __init__(self, **kwargs):
        """Create screens and associated menu items."""
        super().__init__(**kwargs)
        _ = setlocale()
        self.screens_icons = {
            _("Mood"): "emoticon-outline",
            _("Sleep"): "sleep",
            _("Food"): "food-apple-outline",
            _("Activity"): "arm-flex-outline",
        }

        self._screen_manager = ScreenManager()
        self._navigation_drawer = MDNavigationDrawer()
        menu_box = MDBoxLayout(
            orientation="vertical",
            padding="8dp",
            spacing="8dp",
        )
        menu_scroll_view = ScrollView()
        menu_list_items = MDList()

        for screen_name, icon in self.screens_icons.items():
            list_item = OneLineIconListItem(
                text=screen_name,
                on_press=partial(self._set_screen, screen_name),
            )
            screen = RateScreen(
                name=screen_name
            )
            self._screen_manager.add_widget(screen)
            list_item.add_widget(IconLeftWidget(icon=icon))
            menu_list_items.add_widget(list_item)

        menu_scroll_view.add_widget(menu_list_items)
        menu_box.add_widget(menu_scroll_view)
        self._navigation_drawer.add_widget(menu_box)
        self.add_widget(self._screen_manager)
        self.add_widget(self._navigation_drawer)

    def _set_screen(self, screen_name: str, *_):
        """Change current screen."""
        self._navigation_drawer.set_state("close")
        self._screen_manager.current = screen_name

    @property
    def screen_manager(self):
        """Return screen manager."""
        return self._screen_manager


class MainApp(MDApp):
    """Main class that controls communication between widgets, components and storage."""

    def __init__(
        self,
        storage_path=_module_dir("storage.dict"),
        **kwargs
    ):
        """Init this class."""
        super().__init__(**kwargs)

        self.storage = Storage(storage_path)
        _ = setlocale()
        self.init_widgets()
        self.hello = _("Welcome to\n[b]}{avau![/b]")
        self.start = _("Start!")
        self.rate = _("Rate us")
        self.footer = _("[u][size=24][b]Powered by[/b][/size][/u]\nSuccessContent")
        self.day_rate = _("Rate this day mood")
        self.title = _("}{avau")
        self.submit = _("Submit")
        self.theme_cls.primary_palette = "Green"  # "Purple", "Red"

    def on_start(self):
        """Run after the application was built, but not started yet."""
        super().on_start()
        if not self.storage.inited():
            self.storage.set_inited()
            greeting_card = GreetingCard()
            greeting_card.open()

    #def init_storage(self):
    #    """Fill storage for the first run."""
    #    if not self.storage.exists("init"):
    #        # init storage
    #        self.storage.put("init", launch_time=0)
    #        self.storage.put("mood_history", values=[])
    #    else:
    #        init = self.storage.get("init")
    #        init["launch_time"] += 1
    #        self.storage.put("init", **init)

    @staticmethod
    def init_widgets():
        """Load kv files for each widget."""
        for widget in [RateScreen, GreetingCard, CustomCard]:
            Builder.load_string(widget.get_descritpion())

    def callback(self, event: str, addtional_info: dict = None):
        """Process callbacks with communications between widgets."""
        print(f"Event! {event}")
        print(f"Value! {addtional_info}")
        widget, event_type = event.split(".")
        if widget == "HelloScreen":
            if event_type == "start":
                self.root.ids.screen_manager.current = "tipscreen2"


def main():
    """Run the application."""
    MainApp().run()

if __name__ == "__main__":
    main()

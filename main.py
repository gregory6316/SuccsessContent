"""File with application entry point and intercomponents communication controller."""

from kivy.lang import Builder
from kivy.storage.dictstore import DictStore
from kivy.uix.screenmanager import ScreenManager
from  kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
import locale
import gettext
from widgets.mood_screen import MoodScreen
from widgets.mood_rating import MoodRating

"""
.. module:: main
   :synopsis: 
       Main module for connecting widgets and running app

.. moduleauthor:: SuccsessContent <github.com/SuccsessContent>


"""

def setlocale(loc=None):
    
    """
      
      
    **setlocale**

    Function for setting locale


    """

    if loc is None:
        l = locale.getdefaultlocale()[0]
    else:
        l = loc
    lc = gettext.translation('main', localedir='locales', languages=[l])
    lc.install()
    return lc.gettext, lc.ngettext
 
class HelloScreenManager(ScreenManager):
    """

    **HelloScreenManager**

    Screen Manager with action on first run of app.


    """


    def __init__(self, **kwargs):
        """Init this class."""
        super().__init__(**kwargs)
    #Do not delete!
    #def __init__(self, **kwargs):
    #    super().__init__(**kwargs)
    #
    #    mood_screen = MoodScreen(
    #        inited = False,
    #        name = "hello screen"
    #    )

        #mood_screen.add_widget(
        #    CurrentState('emoticon-outline', 'Hello')
        #)
        #sleep_screen = SleepScreen(
        #    name = "sleep screen"
        #)
        #
        #food_screen = FoodScreen(
        #    name = "food screen"
        #)
        #
        #activity_screen = ActivityScreen(
        #    name = "activity screen"
        #)
        #self.add_widget(mood_screen)
        #self.add_widget(sleep_screen)
        #self.add_widget(food_screen)
        #self.add_widget(activity_screen)

class MainApp(MDApp):
    """

    **MainApp**

    Main class that controls communication between widgets, components and storage.


    """


    def __init__(self, **kwargs):
        """Init this class."""
        super().__init__(**kwargs)
        _, ngettext = setlocale()
        self.storage = DictStore("storage.dict")
        self.inited = False
        #self.init_storage()
        self.init_widgets()
        self.title = _("}{avau")
        self.mood_button = _("Mood")
        self.sleep_button = _("Sleep")
        self.food_button = _("Food")
        self.activity_button = _("Activity")
        self.hi = _("Welcome to\n[b]}{avau![/b]")
        self.start = _("Start!")
        self.rate = _("Rate us")
        self.company = _("[u][size=24][b]Powered by[/b][/size][/u]\nSuccessContent")
        self.theme_cls.primary_palette = "Green"  # "Purple", "Red"

    #def init_storage(self):
    #    """Fill storage for the first run."""
    #    if not self.storage.exists("inited"):
    #        # init storage
    #        self.storage.put("inited", values=1)
    #        self.storage.put("mood_history", values=[])

    @staticmethod
    def init_widgets():
        """

        **init_widgets**

        Load kv files for each widget.


        """

        for widget in [MoodScreen, MoodRating]:
            Builder.load_string(widget.get_descritpion())

    #def callback(self, event: str, addtional_info: dict = None):
    #    """Process callbacks with communications between widgets."""
    #    print(f"Event! {event}")
    #    print(f"Value! {addtional_info}")
    #    widget, event_type = event.split(".")
    #    if widget == "HelloScreen":
    #        if event_type == "start":
    #            self.root.ids.screen_manager.current = "tipscreen2"
    #    elif widget == "MoodRating":
    #        pass

def main():
    """

        **main**

        Run the application.


    """

    MainApp().run()

if __name__ == "__main__":
    main()

"""File with application entry point and intercomponents communication controller."""

from kivy.lang import Builder
from kivy.storage.dictstore import DictStore
from kivymd.app import MDApp
from widgets.hello_screen import HelloScreen
from widgets.mood_rating import MoodRating


class MainApp(MDApp):
    """Main class that controls communication between widgets, components and storage."""

    def __init__(self, **kwargs):
        """Init this class."""
        super().__init__(**kwargs)
        self.storage = DictStore("storage.dict")


    def init_storage(self):
        """Fill storage for the first run."""
        if not self.storage.exists("inited"):
            # init storage
            self.storage.put("inited", values=1)
            self.storage.put("mood_history", values=[])

    @staticmethod
    def init_widgets():
        """Load kv files for each widget."""
        for widget in [HelloScreen, MoodRating]:
            Builder.load_string(widget.get_descritpion())

    def build(self):
        """Build current application."""
        self.theme_cls.primary_palette = "Green"  # "Purple", "Red"
        self.init_storage()
        self.init_widgets()

        root = Builder.load_file("main.kv")
        return root

    def callback(self, event: str, addtional_info: dict = None):
        """Process callbacks with communications between widgets."""
        print(f"Event! {event}")
        print(f"Value! {addtional_info}")
        widget, event_type = event.split(".")
        if widget == "HelloScreen":
            if event_type == "start":
                self.root.ids.screen_manager.current = "tipscreen2"
        elif widget == "MoodRating":
            pass


def main():
    """Run the application."""
    MainApp().run()


if __name__ == "__main__":
    main()

"""Welcome Screen."""

import pkgutil
from kivymd.uix.floatlayout import MDFloatLayout


class HelloScreen(MDFloatLayout):
    """Container for Welcome Screen content."""

    def __init__(self, **kwargs):
        """Init basics."""
        # make sure we aren't overriding any important functionality
        super().__init__(**kwargs)

    @staticmethod
    def get_descritpion() -> str:
        """Return kv description content."""
        return pkgutil.get_data(__name__, "description.kv").decode("utf-8")

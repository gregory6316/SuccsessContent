"""Pop-up card with greetings info."""

import pkgutil
from kivy.uix.modalview import ModalView
from kivymd.uix.card import MDCard


class GreetingCard(MDCard, ModalView):
    """Card with greetings message in first run of app.

    Code is in description.kv file.

    Contains:
        "Welcome to }{avau" message.
        "Start!" button: closes greetin card.
        "Rate us" button: allows user to rate the app.
        "Powered by" message.
    """

    def __init__(self, **kwargs):
        """Init greetings card."""
        super().__init__(**kwargs)
        print("TODO RateUs button")

    @staticmethod
    def get_descritpion() -> str:
        """Return kv description content."""
        return pkgutil.get_data(__name__, "description.kv").decode("utf-8")

    # @staticmethod
    # def animate_open_card(widget):
    #     """Animate greetins card's opening.

    #     Args:
    #     widget - greetings card.

    #     Returns:
    #     None.
    #     """
    #     animation = Animation(
    #         pos_hint={"center_y": 0.6}
    #     )
    #     animation.start(widget)

    # def animate_close_card(self, widget):
    #     """Animate greetins card's closing.

    #     Args:
    #     widget - greetings card

    #     Returns:
    #     None
    #     """
    #     animation = Animation(
    #         pos_hint={"center_y": -0.5}
    #     )
    #     animation.bind(on_complete=\
    #         lambda *x: widget.dismiss(animation=True))
    #     animation.start(widget)

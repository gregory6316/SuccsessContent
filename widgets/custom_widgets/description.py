"""Module with custom cards."""
from datetime import datetime, date, timedelta
from calendar import monthrange
import pkgutil
import matplotlib.pyplot as plt
import numpy as np

from kivymd.uix.textfield import MDTextField
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior

from garden_matplotlib.backend_kivyagg import FigureCanvasKivyAgg

class CustomCard(MDCard, RoundedRectangularElevationBehavior):
    """Base class for scrollable cards in screens."""

    def __init__(self, **kwargs):
        """Init this class. Sets radius for card, and independence of size from window."""
        super().__init__(**kwargs)
        self.radius = [20]
        self.size_hint_y = None
        self.size_hint_x = 0.8
        self.pos_hint = {"center_x": 0.5}

    @staticmethod
    def get_descritpion() -> str:
        """Return kv description content."""
        return pkgutil.get_data(__name__, "description.kv").decode("utf-8")


class LabelUnderIconWidget(MDBoxLayout):
    """Widget to paste IconButton and Label vertically."""

    def __init__(self, icon, text, **kwargs):
        """Init this widget.

        Adds MDIconButton and MDLabel vertically.
        Sets on_press to MDIconButton.
        """
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.image = MDIconButton(
            icon=icon,
            pos_hint={"center_x": 0.5},
        )

        self.label = MDLabel(
            text=text,
            halign="center"
        )

        self.add_widget(self.image)
        self.add_widget(self.label)

class CurrentDayCard(CustomCard):
    """Card with icon, current date and some message."""

    def __init__(self, icon="emoticon-outline", msg="", **kwargs):
        """Init this card.

        Sets 'emoticon-outline' icon as default.
        Sets empty message as default.
        """
        super().__init__(**kwargs)

        self.height = 80
        self.need_update = False

        today = datetime.now()
        self.day = today.day
        self.weekday = today.strftime("%A")
        self.month = today.strftime("%b")

        self.icon = icon
        self.msg = msg

        left_icon = MDIconButton(
            icon=self.icon,
            pos_hint={"center_y": 0.5}
        )

        date_cheer_label = MDLabel(
            text=str(self.weekday) + ", " + \
                str(self.day) + " " + str(self.month) + \
                "\n" + self.msg,
        )

        self.add_widget(left_icon)
        self.add_widget(date_cheer_label)

class DaysInRowCard(CustomCard):
    """Card with title and list of 6 last days, their states, and current day with empty state."""

    def __init__(self, storage, key, **kwargs):
        """Init card."""
        super().__init__(**kwargs)

        self.widget = None
        self.need_update = True

        self.orientation = "vertical"
        self.height = 120

        self.storage = storage
        self.key = key

        title = MDLabel(
            text="Days in a Row",
            size_hint_y=None,
            height=40,
            padding=(15, 0)
        )

        self.add_widget(title)
        self.update()

    def update(self):
        """Update the current state of widget."""
        days_layout = MDBoxLayout(
            orientation="horizontal",
            padding=(0, 0, 0, 15)
        )

        today = date.today()
        days = [today - timedelta(days=i) for i in range(6, -1, -1)]

        history_dict = self.storage.get(self.key)
        for day in days:
            icon = "circle-outline"
            if day in history_dict.keys():
                icon = "check-circle-outline"
            days_layout.add_widget(
                LabelUnderIconWidget(
                    icon=icon,
                    text=day.strftime("%a")
                )
            )

        if self.widget:
            self.remove_widget(self.widget)
        self.widget = days_layout
        self.add_widget(self.widget)


class StarButtonsContainer(MDBoxLayout):
    """Container with several star buttons."""

    def __init__(self, stars_count=5, **kwargs):
        """Init container and create star buttons."""
        super().__init__(**kwargs)
        self.stars_count = stars_count

        for i in range(int(self.stars_count)):
            self.add_widget(StarButton(value=i+1))


class StarButton(MDIconButton):
    """Button with star icon, should be combined in one container without other elements."""

    def __init__(self, value, **kwargs):
        """Init StarButton."""
        super().__init__(**kwargs)
        self.value = value
        # scale = 2
        # self.children[0].font_size *= scale
        # self.height *= scale
        # self.width *= scale
        # self.children[0].size = self.size

    def handle_click(self):
        """Handle click on button, change state of other buttons in this container."""
        for widget in self.parent.children:
            widget.icon = "star-outline" if widget.value > self.value else "star"

        storage = self.parent.parent.storage
        key = self.parent.parent.key
        storage.put(key, date.today(), self.value, "")

        self.parent.parent.parent.parent.parent.update()


class RateHabit(CustomCard):
    """Card to rate your habit today."""

    def __init__(self, storage, key, **kwargs):
        """Init card."""
        super().__init__(**kwargs)
        self.storage = storage
        self.key = key
        self.height = 120
        self.need_update = False


class CommentTextField(MDTextField):
    """Text field for comment about day."""

    def __init__(self, **kwargs):
        """Init comment text field."""
        super().__init__(**kwargs)
        self.hint_text = "Дополнительный комментарий"


class Chart(CustomCard):
    """MatPlot of habbit."""

    def __init__(self, storage, key, **kwargs):
        """Init chart."""
        super().__init__(**kwargs)
        self.widget = None
        self.need_update = True
        self.padding = (10, 0, 10, 0)
        self.storage = storage
        self.key = key

        self.update()

    def update(self):
        """Update chart."""
        history = self.storage.get(self.key)

        today = date.today()
        #months = [(today - timedelta(days=30*i)).strftime("%b") for i in range(5, -1, -1)]

        first_month = (today.month + 7) % 12
        if first_month == 0:
            first_month = 12
        first_year = today.year-1 if first_month > today.month else today.year
        first_day = date(day=1, month=first_month, year=first_year)

        values = []
        for _ in range(6): # 6 months
            month_values = []
            for day in range(1, 32):
                if day < monthrange(first_day.year, first_day.month)[1]:
                    if first_day in history.keys():
                        value = history[first_day]['value']
                    else:
                        value = 0
                    first_day += timedelta(days=1)
                else:
                    value = 0
                month_values.append(value)
            values.append(month_values)
        values = np.array(values)

        fig, axis = plt.subplots()
        axis.imshow(values)
        axis.set_xticks(np.arange(31), labels=list(range(1, 32)))
        axis.set_yticks(np.arange(6), labels=
                        [(today - timedelta(days=30*i)).strftime("%b") for i in range(5, -1, -1)])

        plt.setp(axis.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")

        for i in range(6):
            for j in range(31):
                axis.text(j, i, values[i, j],
                          ha="center", va="center", color="w")

        axis.set_title("Mood rating over 6 month")
        fig.tight_layout()
        if self.widget:
            self.remove_widget(self.widget)
        self.widget = FigureCanvasKivyAgg(plt.gcf())
        self.add_widget(self.widget)


class Achievements(CustomCard):
    """Card with achievements."""

    def __init__(self, **kwargs):
        """Init card."""
        super().__init__(**kwargs)


class Count(CustomCard):
    """Count statistics."""

    def __init__(self, **kwargs):
        """Init card."""
        super().__init__(**kwargs)

class Calendar(CustomCard):
    """Simple Calendar."""

    def __init__(self, **kwargs):
        """Init card."""
        super().__init__(**kwargs)
        self.need_update = True

"""Module with custom cards."""
import calendar
from datetime import datetime, timedelta
import pkgutil
import matplotlib.pyplot as plt
import numpy as np

from kivy.storage.dictstore import DictStore
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

    @staticmethod
    def get_descritpion() -> str:
        """Return kv description content."""
        return pkgutil.get_data(__name__, "description.kv").decode("utf-8")


class LabelUnderIconWidget(MDBoxLayout):
    """Widget to paste IconButton and Label vertically."""

    def change_icon(self, new_icon: str) -> None:
        """Change button icon to new icon.

        Args:
        new_icon: str - new icons kivymd name.

        Returns:
        None.
        """
        print("Day is marked")
        self.image.icon = new_icon

    def __init__(self, icon, text, new_icon_on_action=None, **kwargs):
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

        if new_icon_on_action:
            self.image.on_press = lambda *x: \
                self.change_icon(new_icon_on_action)

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

    def __init__(self, storage=None, **kwargs):
        """Init card."""
        if not storage:
            print("TODO storage")

        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.height = 120

        title = MDLabel(
            text="Days in a Row",
            size_hint_y=None,
            height=40,
            padding=(15, 0)
        )

        days_layout = MDBoxLayout(
            orientation="horizontal",
            padding=(0, 0, 0, 15)
        )

        today = datetime.now().weekday()
        days = [calendar.day_name[today - i] for i in range(6, 0, -1)]

        for day in days:
            days_layout.add_widget(
                LabelUnderIconWidget(
                    icon="check-circle-outline",
                    text=day[:3]
                )
            )

        today_widget = LabelUnderIconWidget(
            icon="checkbox-blank-circle-outline",
            text=calendar.day_name[today][:3],
            new_icon_on_action="check-circle-outline"
        )

        days_layout.add_widget(today_widget)

        self.add_widget(title)
        self.add_widget(days_layout)


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
        storage = DictStore("storage.dict")
        if not storage.exists("init"):
            # init storage
            storage.put("init", launch_time=0)
            storage.put("mood_history", init=True)
        else:
            init = storage.get("init")
            init["launch_time"] += 1
            storage.put("init", **init)
        mood_history = storage.get("mood_history")
        mood_history[datetime.now().strftime("%d, %B")] = self.value
        storage.put("mood_history", **mood_history)
        self.parent.parent.parent.parent.parent.chart.update()


class RateHabit(CustomCard):
    """Card to rate your habit today."""

    def __init__(self, **kwargs):
        """Init card."""
        super().__init__(**kwargs)
        print("Тут должен оцениваться сегодняшний habit")


class CommentTextField(MDTextField):
    """Text field for comment about day."""

    def __init__(self, **kwargs):
        """Init comment text field."""
        super().__init__(**kwargs)
        self.hint_text = "Дополнительный комментарий"


class Chart(CustomCard):
    """MatPlot of habbit."""

    def __init__(self, **kwargs):
        """Init chart."""
        super().__init__(**kwargs)
        self.widget = None
        self.update()

    def update(self):
        """Update chart."""
        today = datetime.now()
        months = [(today - timedelta(30*i)).strftime('%B') for i in range(5, -1, -1)]
        days = [str(i) if i > 9 else '0' + str(i) for i in range(1, 32)]
        storage = DictStore("storage.dict")
        mood_history = storage.get("mood_history")
        mood = []
        for i in months:
            month = []
            for j in days:
                if str(j) + ', ' + str(i) in mood_history.keys():
                    month.append(mood_history[str(j) + ', ' + str(i)])
                else:
                    month.append(0)
            mood.append(month)
        mood = np.array(mood)

        fig, axis = plt.subplots()
        axis.imshow(mood)
        axis.set_xticks(np.arange(len(days)), labels=days)
        axis.set_yticks(np.arange(len(months)), labels=months)

        plt.setp(axis.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

        for i in range(len(months)):
            for j in range(len(days)):
                axis.text(j, i, mood[i, j],
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
        print("Можно ачивки сделать, и их здесь выводить")


class Count(CustomCard):
    """Count statistics."""

    def __init__(self, **kwargs):
        """Init card."""
        super().__init__(**kwargs)
        print("Здесь просто выводится статистика " + \
            "по каждой оценке: сколько раз оценка 5, ...")

class Calendar(CustomCard):
    """Simply Calendar."""

    def __init__(self, **kwargs):
        """Init card."""
        super().__init__(**kwargs)
        print("Просто каледнарь с отметками о днях")

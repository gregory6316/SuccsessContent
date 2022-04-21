"""Screen with mood rating slider and chart."""

import pkgutil
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.slider import MDSlider
from kivy_garden.graph import MeshLinePlot
import locale
import gettext

"""
.. module:: mood_rating
   :synopsis: 
       Module for mood rating

.. moduleauthor:: SuccsessContent <github.com/SuccsessContent>


"""

def setlocale(loc=None):
    if loc is None:
        l = locale.getdefaultlocale()[0]
    else:
        l = loc
    lc = gettext.translation('mood_rating', localedir='locales', languages=[l])
    lc.install()
    return lc.gettext, lc.ngettext

class MoodRating(MDBoxLayout):
    """

    **MoodRating**

    Screen with mood rating slider and chart.


    """
    def __init__(self, **kwargs):
        """

        **MoodRating.__init__**

        Init this class.


        """
        super().__init__(**kwargs)
        _, ngettext = setlocale()
        self.rate = _("Remove last rate")
        self.x_label = _("Mood rate")

    @staticmethod
    def get_descritpion() -> str:
        """

        **MoodRating.get_descritpion**

        Return content of description kv.


        """
        return pkgutil.get_data(__name__, "description.kv").decode("utf-8")


class MoodSlider(MDSlider):
    """

    **MoodSlider**

    Slider for mood rating.


    """


    def __init__(self, **kwargs):
        """

        **MoodSlider.get_descritpion**

        Init basics and register events.


        """

        self.register_event_type('on_slider_release')
        super().__init__(**kwargs)

    def on_slider_release(self):
        """

        **MoodSlider.on_slider_release**

        Do nothing. We should declare func for each event.


        """

    def on_touch_up(self, touch):
        """

        **MoodSlider.on_touch_up**

        Dispatch event on_slider_release if only touch up triggered by this class.


        """
        super().on_touch_up(touch)
        if touch.grab_current == self:
            self.dispatch('on_slider_release')

    @staticmethod
    def set_callback(value, storage, graph_box) -> None:
        """

        **MoodSlider.set_callback**

        Update storage and redraw chart.


        """
        mood_history = storage.get("mood_history")
        mood_history["values"].append(value)
        storage.put("mood_history", **mood_history)

        # graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
        # x_ticks_major=25, y_ticks_major=1,
        # y_grid_label=True, x_grid_label=True, padding=5,
        # x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
        if not graph_box.plots:
            plot = MeshLinePlot(color=[1, 0, 0, 1])
            graph_box.add_plot(plot)
        graph_box.plots[0].points = list(enumerate(mood_history["values"]))

.. }{avau! documentation master file, created by
   sphinx-quickstart on Tue Jun 14 06:40:06 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

}{avau by SuccsessContent
*************************************

Python collaborative project for uneex course

**}{avau** is a mobile application for daily tracking of habbits, moods, exercises, and many more!

Opportunities
================================
**}{avau** is professional self-imporvement mentor-app. It can track many sides of your life, helping you in becoming the better version of yourself.

* Make reflections of your daily life
* Analyze your habbits
* Analyze your sleeping
* Track the food you eat everyday
* Start and track exercising in your tempo
* Gather and explore your daily/weekly/mothly/year statistics
* Enjoy the pretty graphics

Architecture
================================
The application consists of 4 parts:

1. Application's main loop. It's the key part, hadnling the main loop and the entire data transfer between other parts.

2. Logic part, including BaseTracker and it's derivatives. BaseTracker is the main class of daily custom habbit trackers. The classes SleepingTracker, ..., correspond to narrow tasks of relevant habbit tracking.

3. Database handling part, including sqlite database, that stores users daily data. Also pandas library is used to gather statistics from data.

4. GUI part, implemented via kivy, kivymd. It gets users prompt (e.g., pressing buttons, inputing texts, ets), and displays different graphics, plotted via pyplot/seaborn.

Also, the application can export data and statistics in wide range of extensions. Implemented via pandas.



Installation
================================
How to init repository:

```
(bash)
pip install -r requirements.txt
pre-commit install
```




Welcome to }{avau!'s documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

}{avau main
===================================
.. automodule:: main
   :members:
   :noindex:
   :synopsis: 
       File with application entry point and intercomponents communication controller.


}{avau custom_widgets
===================================
.. automodule:: widgets.custom_widgets.description
   :members:
   :synopsis: 
       Module with custom cards.

}{avau mood_screen
===================================
.. automodule:: widgets.mood_screen.description
   :members:
   :synopsis: 
       Rate Screen.

}{avau greeting_card
===================================
.. automodule:: widgets.greeting_card.description
   :members:
   :synopsis: 
       Pop-up card with greetings info.

Indices and tables
===================================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

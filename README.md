# }{avau by SuccsessContent

<img src = "./img/logo.png" align="right"
  alt="SuccessContent Team" width="120" height="120">

Python collaborative project for uneex course

}{avau is a mobile application for daily tracking of habbits, moods, exercises, and many more!

## Opportunities
}{avau is professional self-imporvement mentor-app. It can track many sides of your life, helping you in becoming the better version of yourself.

* Make reflections of your daily life
* Analyze your habbits
* Analyze your sleeping
* Gather and explore your mothly/year statistics

## Architecture

<p align="center">
  <img src="https://github.com/Temish09/SuccsessContent/blob/main/img/Architecture.png" alt="Architecture" width="738">
</p>

The application consists of 4 parts:
* Application's main loop. It's the key part, handling the main loop and the entire data transfer between other parts.
* Logic part, including tracking the habits functionality behind widgets.
* Database handling part, including kivy DictStore, that stores users daily data. 
* GUI part, implemented via kivy, kivymd. It gets users prompt (i.e., inputing ratings, texts, ets), and displays different graphics.

## UI
The preliminary UI concept can be found below.

[UI concept](https://www.figma.com/file/FXHWjqIN4tdKqDirSu9XrQ/Untitled?node-id=0%3A1)

## Installation
How to init repository:
(bash)
pip install -r requirements.txt
pre-commit install

## Other
Commit messages style: https://habr.com/ru/post/183646/

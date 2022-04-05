from turtle import Screen, Turtle

"""
.. module:: display
   :synopsis: Данный модуль релизует рисование черепашкой

.. moduleauthor:: SuccsessContent <github.com/SuccsessContent>
"""
def create_turtle(pixel_size):
    """
        **create_turtle**

        Данная функция инициализирует черепаху

        :return: черепаху

        - Example::
            
            Воот такую черепаху возвращает

        - Expected Success Response::

            Вот еще одна потерялась
            --░░░░        ▓▓▓▓▓▓▓▓▓▓      
            ░░░░░░░░    ▓▓▒▒▒▒░░▒▒▒▒▓▓    
            ░░██░░░░  ▓▓░░▒▒▒▒▓▓▒▒▒▒░░▓▓  
            ░░░░░░░░▓▓▒▒▒▒░░▓▓▓▓▓▓░░▒▒▒▒▓▓
            --░░░░░░▓▓▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒▓▓
            ----░░░░▒▒░░▓▓▓▓▒▒░░▒▒▓▓▓▓░░▓▓
            ----░░░░▓▓▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▓▓
            ------░░▓▓▒▒▒▒░░▓▓▓▓▓▓░░▒▒▒▒▓▓
            ---------▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
            ---------░░░░░░      ░░░░░░  
            ---------░░░░░░      ░░░░░░ 

    
    """
    turtle = Turtle()
    turtle.shape("square")
    turtle.shapesize(pixel_size / 20, pixel_size / 20)
    turtle.hideturtle()
    turtle.up()

    return turtle


def create_screen(title, width, height):
    """
        **create_screen**

        Данная функция инициализирует экран

        :return: экран для черепашки

        - Example::

            Экран никогда не видел???

        - Expected Success Response::

            --░░░░        ▓▓▓▓▓▓▓▓▓▓      
            ░░░░░░░░    ▓▓▒▒▒▒░░▒▒▒▒▓▓    
            ░░██░░░░  ▓▓░░▒▒▒▒▓▓▒▒▒▒░░▓▓  
            ░░░░░░░░▓▓▒▒▒▒░░▓▓▓▓▓▓░░▒▒▒▒▓▓
            --░░░░░░▓▓▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒▓▓
            ----░░░░▒▒░░▓▓▓▓▒▒░░▒▒▓▓▓▓░░▓▓
            ----░░░░▓▓▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▓▓
            ------░░▓▓▒▒▒▒░░▓▓▓▓▓▓░░▒▒▒▒▓▓
            ---------▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
            ---------░░░░░░      ░░░░░░  
            ---------░░░░░░      ░░░░░░ 

        
    """
    screen = Screen()
    screen.title(title)
    screen.setup(width=width, height=height)
    screen.tracer(0)

    return screen


def draw_pixel(turtle, x, y):
    """
        **draw_pixel**

        Ну тупа ставит точку по координатам
        
    """
    turtle.goto(x, y)
    turtle.stamp()




















import math
from decimal import Decimal, getcontext

"""
.. module:: formula
   :synopsis: Данный модуль реализует самореферентную формулу Таппера

.. moduleauthor:: SuccsessContent <github.com/SuccsessContent>


"""
getcontext().prec = 10000


def should_pixel_be_drawn(x, y):
    """
       **should_pixel_be_drawn**
        Данная функция по формуле Таппера определяет нужно ли ставить точку в данной точке(точка).
        :return: True или False
    

    """
    power_of_two = -17 * math.floor(x) - math.floor(y) % 17
    formula = math.floor((math.floor(Decimal(y)/17) * (2 ** Decimal(power_of_two))) % 2)

    return formula > 0.5
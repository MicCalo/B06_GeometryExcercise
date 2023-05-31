from painter import Painter
from shape import Shape
import math


class Ellipse(Shape):
    def __init__(self, x, y, color, width, height):
        super().__init__(x, y, color)
        self._width = width
        self._height = height
        

    def calculate_area(self):
        return math.pi * self._x * self._y


    def paint(self, painter: Painter):
        painter.paint_ellipse(self._color, self._x, self._y, self._width, self._height)

# coding: utf8

from painter import Painter
from shape import Shape

class Rectangle(Shape):
    def paint(self, painter: Painter):    
        painter.paint_line(self._color, self._x - self._width / 2, self._y - self._height / 2, self._x + self._width / 2, self._y- self._height / 2)
        painter.paint_line(self._color, self._x + self._width / 2, self._y - self._height / 2, self._x + self._width / 2, self._y + self._height / 2)
        painter.paint_line(self._color, self._x + self._width / 2, self._y + self._height / 2, self._x - self._width / 2, self._y + self._height / 2)
        painter.paint_line(self._color, self._x - self._width / 2, self._y + self._height / 2, self._x - self._width / 2, self._y- self._height / 2)
        
    def calculate_area(self):
        return self._width * self._height
    
    def __init__(self, x, y, color, width, height):
        super().__init__(x, y, color)
        self._width = width
        self._height = height
    
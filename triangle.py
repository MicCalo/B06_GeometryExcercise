#!/usr/bin/env python3
# coding: utf8

from painter import Painter
from shape import Shape

class Triangle(Shape):
    def paint(self, painter: Painter):
        top_x = self._x
        top_y = self._y - self._height / 3 * 2

        left_x = self._x - self._base/2
        left_y = self._y + self._height / 3

        right_x = self._x + self._base/2
        right_y = left_y
        painter.paint_line(self._color, top_x, top_y, left_x, left_y)
        painter.paint_line(self._color, left_x, left_y, right_x, right_y)
        painter.paint_line(self._color,  right_x, right_y, top_x, top_y)
        
    def calculate_area(self):
        return 0.5 * self._base * self._height
    
    def __init__(self, x, y, color, base, height):
        super().__init__(x, y, color)
        self._base = base
        self._height = height
    
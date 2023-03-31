#!/usr/bin/env python3
# coding: utf8

from painter import Painter
from shape import Shape

class Triangle(Shape):
    def paint(self, painter: Painter):
        painter.draw_triangle()

    def calculate_area(self):
        return 0.5 * self._base * self._height
    
    def __init__(self, x, y, color, base, height):
        super().__init__(x, y, color)
        self._base = base
        self._height = heigh
    
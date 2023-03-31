#!/usr/bin/env python3
# coding: utf8

from painter import Painter

class Shape:
    def __init__(self, x,y,color):
        self._x = x
        self._y = y
        self._color = color

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def calculate_area(self):
        pass

    def paint(self, painter: Painter):
        pass
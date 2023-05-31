# coding: utf8

from shape import Shape
from painter import Painter

class Polygon(Shape):
    def __init__(self, x, y, color, points:list=[(-10, -10), (0, -5), (10, -20), (10, 0), (5, 5), (-5, 20)]):
        super().__init__(x, y, color)
        self._points = points

    def calculate_area(self):
       #implementation of shoelace algorithm from https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates
        n = len(self._points) # of corners
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self._points[i][0] * self._points[j][1]
            area -= self._points[j][0] * self._points[i][1]
        area = abs(area) / 2.0
        return area

    def paint(self, painter: Painter):
        for i in range(1, len(self._points)):
            a = self._points[i-1]
            b = self._points[i]
            painter.paint_line(self._color, self._x+a[0], self._y+a[1], self._x+b[0], self._y+b[1])

        # draw line from last to first point (make sure polygon is closed)
        a = self._points[len(self._points)-1]
        b = self._points[0]
        painter.paint_line(self._color, self._x+a[0], self._y+a[1], self._x+b[0], self._y+b[1])

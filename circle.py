#This is my Circle Shape
from painter import Painter
from shape import Shape
import math


class Circle(Shape):

    def __init__(self,x,y,color, radius):
        super().__init__(x, y, color)
        self._radius = radius
    
    def calculate_area(self):
        return math.pi * self._radius ** 2

    def paint(self, painter:Painter):        
        painter.paint_ellipse(self._color, self._x, self._y, self._radius, self._radius)

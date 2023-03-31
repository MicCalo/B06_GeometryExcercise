#This is my Circle Shape
from painter import Painter
import shape
import math


class Circle(shape):
    radius = 0
    def __init__(self,x,y,color):
        super().__init__(x, y, color)
        self.radius = abs(self.x-self.y)
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

    def paint(self, painter:Painter):
        rx = self.x + self.radius 
        ry = self.y + self.radius
        painter.paint_ellipse(self.color, self.x, self.y, rx, ry)

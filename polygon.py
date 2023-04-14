from shape import Shape
from painter import Painter

class Polygon(Shape):
    def __init__(self, x, y, color, number_of_sides):
        super().__init__(x, y, color)
        self.n = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Seite eingeben "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Seite",i+1,"ist",self.sides[i])

    def calculate_area(self):
        return 0

    def paint(self, painter: Painter):
        painter.paint_line(self._color, self._x, self._y, self._x + 100, self._y)

if __name__ == "__main__":
    polygon = Polygon(0, 0, "red", 3)
    polygon.inputSides()
    polygon.dispSides()
    print("Area is", polygon.calculate_area())
    painter = Painter()
    polygon.paint(painter)

    

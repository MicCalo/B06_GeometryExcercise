# coding: utf8

from enum import IntEnum

from shape import Shape
from Shapes.circle import Circle
from Shapes.ellipse import Ellipse
from Shapes.rectangle import Rectangle
from Shapes.triangle import Triangle
from Shapes.polygon import Polygon

from Persistence.connector import Connector

class ShapeType(IntEnum):
    CIRCLE = 1,
    RECTANGLE = 2,
    ELLIPSE = 3,
    TRIANGLE = 4,
    POLYGON = 5



class ShapePersistence:

    def __init__(self, connector: Connector):
        self._connector = connector


    def load(self)->list[Shape]:
        result = []
        for row in self._connector.fetch_all("SELECT * FROM Shapes"):
            id = row[0]
            type = row[1]
            x = row[2]
            y = row[3]
            color = row[4]

            result.append(self._load_shape(id, ShapeType(type), x, y, color))
        return result
    
    def save(self, shapes: list[Shape]):
        id = self._connector.fetch_one("SELECT max(Id) FROM Shapes")[0]
        if not id:
            id = -1
        for shape in shapes:
            id+=1
            type, points = self._get_data(shape)
            self._connector.execute_statement(f"INSERT INTO Shapes (id, type, x, y, color) VALUES ({id}, {int(type)}, {shape._x}, {shape._y}, {shape._color})")
            for i in range(len(points)):
               self._connector.execute_statement(f"INSERT INTO Points (shapeId, position, x, y) VALUES ({id}, {i}, {points[i][0]}, {points[i][1]})")
                
    
    def _get_data(self, shape: Shape)->tuple[ShapeType, list[tuple[int, int]]]:
        points: list[tuple[int, int]] = []
        if isinstance(shape, Circle):
            _type = ShapeType.CIRCLE
            points = [(shape._radius, -1)]
        elif isinstance(shape, Rectangle):
            _type = ShapeType.RECTANGLE
            points = [(shape._width, shape._height)]
        elif isinstance(shape, Ellipse):
            _type = ShapeType.ELLIPSE
            points = [(shape._width, shape._height)]
        elif isinstance(shape, Triangle):
            _type = ShapeType.TRIANGLE
            points = [(shape._base, shape._height)]
        elif isinstance(shape, Polygon):
            _type = ShapeType.POLYGON
            points =shape._points
        else:
            raise TypeError(f"Shape of  type '{type(shape)}' not supported")
        return (_type, points)


    def _load_shape(self, shape_id: int, type:ShapeType, x:int, y:int, color:int):
        points = self._load_points(shape_id)
        if type == ShapeType.CIRCLE:
            assert(len(points) == 1)
            return Circle(x, y, color, points[0][0])
        elif type == ShapeType.RECTANGLE:
            assert(len(points) == 1)
            return Rectangle(x, y, color, points[0][0], points[0][1])
        elif type == ShapeType.ELLIPSE:
            assert(len(points) == 1)
            return Ellipse(x, y, color, points[0][0], points[0][1])
        elif type == ShapeType.TRIANGLE:
            assert(len(points) == 1)
            return Triangle(x, y, color, points[0][0], points[0][1])
        elif type == ShapeType.POLYGON:
            assert(len(points) > 2)
            return Polygon(x, y, color, points)
        else:
            raise TypeError(f"ShapeType '{type}' not supported")

    def _load_points(self, shape_id: int)->list[tuple[int, int]]:
        points = []
        for row in self._connector.fetch_all(f"SELECT x, y FROM Points WHERE ShapeId={shape_id} ORDER BY Position"):
            points.append(row)
        return points
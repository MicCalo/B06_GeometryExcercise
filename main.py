#!/usr/bin/env python3
# coding: utf8

import json
import logging

import tkinter as tk

from Shapes.circle import Circle
from Shapes.ellipse import Ellipse
from Shapes.rectangle import Rectangle
from Shapes.triangle import Triangle
from Shapes.polygon import Polygon

from Persistence.connector import create_connector, Connector
from Persistence.shape_persistence import ShapePersistence

from Painters.tkinter_painter import TkinterPainter
from Painters.svg_painter import SvgPainter


def initialize_shapes(connector: Connector)->list:
    persistence = ShapePersistence(connector)
    shapes = persistence.load()
    if len(shapes) == 0:
        shapes.append(Triangle( 100, 100, 0xFF0000, 80, 80))
        shapes.append(Circle(   250, 100, 0x228B22, 40))
        shapes.append(Ellipse(  400, 100, 0x1E90FF, 40, 25))
        shapes.append(Rectangle(100, 300, 0xFF00FF, 80, 50))
        shapes.append(Polygon(  400, 300, 0x000080))
        logging.info(f"DB was empty. Added some shapes")
        persistence.save(shapes)
    else:
        logging.info(f"Loaded {len(shapes)} shapes form DB")
    return shapes


def render(shapes: list, painter):
    for shape in shapes:
        painter.paint_line(0, shape._x-3, shape._y-3, shape._x+3, shape._y+3, 1)
        painter.paint_line(0, shape._x+3, shape._y-3, shape._x-3, shape._y+3, 1)
        shape.paint(painter)


def show_tkinter(shapes: list):
    root = tk.Tk()
    root.geometry('800x600+100+100')
    root.title("Geometry Shapes App")

    canvas = tk.Canvas(root, bg='white')
    canvas.pack(expand=True, fill=tk.BOTH)

    painter = TkinterPainter(canvas)
    render(shapes, painter)

    root.mainloop()


def show_svg(shapes: list):
    with SvgPainter("shapes.svg") as painter:
        render(shapes, painter)


def main():
    logging.basicConfig(level=logging.DEBUG)

    # initialize DB
    with open('db_config.json', 'r') as file:
        db_config = json.load(file)
    connector = create_connector(db_config)

    logging.info(f"Create dB Connector: {connector.get_version()}")

    # initialize shapes (load or create some id DB is empty)
    shapes = initialize_shapes(connector)

    show_svg(shapes)

    show_tkinter(shapes)

    

if __name__ == '__main__':
    main()
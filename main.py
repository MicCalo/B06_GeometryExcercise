#!/usr/bin/env python3
# coding: utf8

import json
import logging

from shape import Shape
from circle import Circle
from ellipse import Ellipse
from rectangle import Rectangle
from triangle import Triangle
from polygon import Polygon

from Persistence.connector import create_connector, Connector
from Persistence.shape_persistence import ShapePersistence

def initialize_shapes(connector: Connector):
    persistence = ShapePersistence(connector)
    shapes = persistence.load()
    if len(shapes) == 0:
        shapes.append(Triangle(10, 10, 0xFF0000, 10, 17))
        shapes.append(Circle(50, 10, 0xFFFF00, 20))
        shapes.append(Ellipse(90, 10, 0x00FF00, 15, 30))
        shapes.append(Rectangle(10, 50, 0x00FFFF, 15, 30))
        shapes.append(Polygon(50, 50, 0x0000FF))
        logging.info(f"DB was empty. Added some shapes")
        persistence.save(shapes)
    else:
        logging.info(f"Loaded {len(shapes)} form DB")


def main():
    logging.basicConfig(level=logging.DEBUG)

    # initialize DB
    with open('db_config.json', 'r') as file:
        db_config = json.load(file)
    connector = create_connector(db_config)

    logging.info(f"Create dB Connector: {connector.get_version()}")

    # initialize shapes (load or create some id DB is empty)
    initialize_shapes(connector)

    

if __name__ == '__main__':
    main()
# coding: utf8

from tkinter import Canvas
from painter import Painter


class TkinterPainter(Painter):
    def __init__(self, canvas: Canvas):
        self._canvas = canvas

    def paint_line(self, color, x1, y1, x2, y2, width=2):
        self._canvas.create_line(x1, y1, x2, y2, fill=TkinterPainter.to_tkinter_color(color), width=width)

    def paint_ellipse(self, color, x, y, rx, ry, width=2):
        self._canvas.create_oval(x-rx, y-ry, x+rx, y+ry, outline=TkinterPainter.to_tkinter_color(color), width=width)

    @staticmethod
    def to_tkinter_color(rgb: int) -> str:
        return f'#{rgb:06x}'

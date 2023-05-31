# coding: utf8

from tkinter import Canvas
from painter import Painter


class TkinterPainter(Painter):
    def __init__(self, canvas: Canvas):
        self._canvas = canvas

    def paint_line(self, color, x1, y1, x2, y2):
        self._canvas.create_line(x1, y1, x2, y2, fill=TkinterPainter.to_tkinter_color(color))

    def paint_ellipse(self, color, x, y, rx, ry):
        self._canvas.create_oval(x-rx/2, y-ry/2, x+rx/2, y+ry/2, outline=TkinterPainter.to_tkinter_color(color))

    @staticmethod
    def to_tkinter_color(rgb: int) -> str:
        return f'#{rgb:06x}'

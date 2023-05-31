# coding: utf8

from painter import Painter


class SvgPainter(Painter):
    def __init__(self, file_name: str):
        self._file_name = file_name

    def __enter__(self):
        self._file = open(self._file_name, 'w')
        self._file.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n')
        #self._file.write('  <rect x="0" y="0" width="100%" height="100%" fill="black"/>\n')
        return self
    
    def __exit__(self, *args):        
        #self._file.write('  </rect>\n')
        self._file.write('</svg>\n')
        self._file.close()

    def paint_line(self, color, x1, y1, x2, y2, width=2):
         self._file.write(f'    <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{SvgPainter.to_svg_color(color)}" stroke-width="{width}" />\n')

    def paint_ellipse(self, color, x, y, rx, ry, width=2):
         self._file.write(f'    <ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" stroke="{SvgPainter.to_svg_color(color)}" stroke-width="{width}" fill-opacity="0" />\n')

    @staticmethod
    def to_svg_color(rgb: int) -> str:
        return f'#{rgb:06x}'

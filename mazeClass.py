from windowClasses import *
from cellClass import *

class Maze:
    def __init__(self,rows, cols, xSize, ySize, x1=0, y1=0, win=None):
        self._x1 = x1
        self._y1 = y1
        self.rows = rows
        self.cols = cols
        self.xSize = xSize
        self.ySize = ySize
        self.win = win

        self._create_cells()
    def _create_cells(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self._draw_cell(i, j)

    def _draw_cells(self, i, j):
        topLeft = Point(self._x1 + (i * self.xSize), self.y1 + (i * self.ySize))
        topRight = Point(self._x1 + ((i + 1) * self.xSize), self.y1 + (i * self.ySize) )
        bottomLeft = Point(self._x1 + (i * self.xSize), self._y1)
        bottomRight = Point(self._x1 + ((i + 1) * self.xSize),)
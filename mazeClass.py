from windowClasses import *
from cellClass import *
from time import time
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
                self._draw_cells(i, j)

    def _draw_cells(self, i, j):
        topLeft = self._x1 + (i * self.xSize)
        topRight = self._y1 + (j * self.ySize)
        bottomLeft = self._x1 + (i * self.xSize)
        bottomRight = self._y1 + ((j + 1) * self.ySize)
        newCell = Cell(topLeft, topRight, bottomLeft, bottomRight, self.win)
        newCell.draw(newCell.x1, newCell.y1, newCell.x2, newCell.y2, self.win._canvas, "purple")
        self._animate()

    def _animate(self):
        self.win.redraw()
        #time.sleep(0.05)
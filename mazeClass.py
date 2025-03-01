from windowClasses import *
from cellClass import *
import time
class Maze:
    def __init__(self,rows, cols, xSize, ySize, x1=0, y1=0, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self.rows = rows
        self.cols = cols
        self.xSize = xSize
        self.ySize = ySize
        self.win = win
        self.list = []
        self.seed = seed

        self._create_cells()
        self._break_entrance_and_exit()
    def _create_cells(self):
        for i in range(self.cols):
            self.list.append([])
            for j in range(self.rows):
                self._draw_cells(i, j)

    def _draw_cells(self, i, j):
        if self.win == None:
            return
        topLeft = self._x1 + (i * self.xSize)
        topRight = self._y1 + (j * self.ySize)
        bottomLeft = self._x1 + (i * self.xSize)
        bottomRight = self._y1 + ((j + 1) * self.ySize)
        newCell = Cell(topLeft, topRight, bottomLeft, bottomRight, self.win)
        self.list[i].extend([newCell])
        newCell.draw(newCell.x1, newCell.y1, newCell.x2, newCell.y2, self.win._canvas, "black")
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        firstIndex = self.list[0][0]
        firstIndex.topWall = False
        firstIndex.draw(firstIndex.x1, firstIndex.y1, firstIndex.x2, firstIndex.y2, self.win._canvas, "white")
        secondIndex = self.list[self.cols - 1][self.rows - 1]
        secondIndex.bottomWall = False
        secondIndex.draw(secondIndex.x1, secondIndex.y1, secondIndex.x2, secondIndex.y2, self.win._canvas, "white")

    def _wall_smasher(self):
        
    def _wall_smasher_r(self, i, j):
        pass

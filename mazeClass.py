from windowClasses import *
from cellClass import *
import random
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
        random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._wall_smasher_r(0, 0)
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
    def _wall_smasher_r(self, i, j):
        toBeVisited = []
        emptyList = []
        currentIndex = self.list[i][j]
        if (i + 1) <= self.rows:
            if self.list[i + 1][j].visited == False:
                toBeVisited.append(self.list[i + 1][j])
                #down
                pass
        if (j + 1) <= self.cols:
            if self.list[i][j+1].visited == False:
                toBeVisited.append(self.list[i][j+1])
                #right
        if (i - 1) >= 0:    
            if self.list[i - 1][j].visited == False:
                toBeVisited.append(self.list[i - 1][j])
                #up
        if (j - 1) >= 0:
            if self.list[i][j - 1].visited == False:
                toBeVisited.append(self.list[i][j - 1])
                #Left
        if not toBeVisited:
            return
        nextCell = toBeVisited[random.randint(0,3)]


        #[0][0], [0]+1[0] = 1 down
        

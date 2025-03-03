from depreciated2.windowClassesOLD2 import *
from depreciated2.cellClassOLD2 import *
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
        self.list[i].append(newCell)
        newCell.draw(newCell.x1, newCell.y1, newCell.x2, newCell.y2, self.win._canvas, "black")
        self._animate(0)

    def _animate(self, delay):
        self.win.redraw()
        time.sleep(delay)

    def _break_entrance_and_exit(self):
        firstIndex = self.list[0][0]
        Line.draw(Line(Point(firstIndex.x1, firstIndex.y1),Point(firstIndex.x1, firstIndex.y2)), self.win._canvas, "white")
        secondIndex = self.list[self.cols - 1][self.rows - 1]
        Line.draw(Line(Point(secondIndex.x1, secondIndex.y2),Point(secondIndex.x2, secondIndex.y1)), self.win._canvas, "white")
    def _wall_smasher_r(self, i, j):
            self._animate(0.5)
            currentIndex = self.list[i][j]
            currentIndex.visited = True
            toBeVisited = []
            while True:
                if (i + 1) < self.rows:
                    if self.list[i + 1][j].visited == False:
                        toBeVisited.append((self.list[i + 1][j],i + 1, j, 1))
                        #down
                if (j + 1) < self.cols:
                    if self.list[i][j+1].visited == False:
                        toBeVisited.append((self.list[i][j+1],i, j + 1, 2))
                        #right
                if (i - 1) >= 0:    
                    if self.list[i - 1][j].visited == False:
                        toBeVisited.append((self.list[i - 1][j],i - 1, j, 3))
                        #up
                if (j - 1) >= 0:
                    if self.list[i][j - 1].visited == False:
                        toBeVisited.append((self.list[i][j - 1],i, j - 1, 4))
                        #Left
                if toBeVisited == []:
                    currentIndex.draw(currentIndex.x1, currentIndex.y1, currentIndex.x2, currentIndex.y2, self.win._canvas, "black")
                    return
                nextNode = toBeVisited[random.randint(0,len(toBeVisited) - 1)]
                if nextNode[3] == 1:
                    nextNode[0].topWall = False
                    currentIndex.bottomWall = False
                    #Line(Point(currentIndex.x1,currentIndex.y2),Point(currentIndex.x2, currentIndex.y2)).draw(self.win._canvas, "white")
                    currentIndex.draw(currentIndex.x1, currentIndex.y1, currentIndex.x2, currentIndex.y2, self.win._canvas, "black")
                if nextNode[3] == 2:
                    currentIndex.rightWall = False
                    nextNode[0].leftWall = False
                    #Line(Point(currentIndex.x2,currentIndex.y1),Point(currentIndex.x2, currentIndex.y2)).draw(self.win._canvas, "white")
                    currentIndex.draw(currentIndex.x1, currentIndex.y1, currentIndex.x2, currentIndex.y2, self.win._canvas, "black")
                if nextNode[3] == 3:
                    currentIndex.topWall = False
                    nextNode[0].bottomWall = False
                    #Line(Point(currentIndex.x1,currentIndex.y1),Point(currentIndex.x2, currentIndex.y1)).draw(self.win._canvas, "white")
                    currentIndex.draw(currentIndex.x1, currentIndex.y1, currentIndex.x2, currentIndex.y2, self.win._canvas, "black")
                if nextNode[3] == 4:
                    currentIndex.leftWall = False
                    nextNode[0].rightWall = False
                    #Line(Point(currentIndex.x1,currentIndex.y1),Point(currentIndex.x1, currentIndex.y2)).draw(self.win._canvas, "white")
                    currentIndex.draw(currentIndex.x1, currentIndex.y1, currentIndex.x2, currentIndex.y2, self.win._canvas, "black")
                if nextNode == self.list[self.cols - 1][self.rows - 1]:
                    return
                self._wall_smasher_r(nextNode[1], nextNode[2])


'''        if not toBeVisited:
            return
        randomValue = random.randint(0, len(toBeVisited) - 1)
        nextCell = (toBeVisited.pop(randomValue))
        nextCell[0].visited = True
        if nextCell[0] == self.list[self.cols-1][self.rows - 1]:
            return
        if nextCell[3] == 1:
            nextCell[0].bottomWall = False
            nextCell[0].draw(nextCell[0].x1, nextCell[0].y1, nextCell[0].x2, nextCell[0].y2, self.win._canvas, "red")
        if nextCell[3] == 2:
            nextCell[0].rightWall = False
            nextCell[0].draw(nextCell[0].x1, nextCell[0].y1, nextCell[0].x2, nextCell[0].y2, self.win._canvas, "red")
        if nextCell[3] == 3:
            nextCell[0].topWall = False
            nextCell[0].draw(nextCell[0].x1, nextCell[0].y1, nextCell[0].x2, nextCell[0].y2, self.win._canvas, "red")
        if nextCell[3] == 4:
            nextCell[0].leftWall = False
            nextCell[0].draw(nextCell[0].x1, nextCell[0].y1, nextCell[0].x2, nextCell[0].y2, self.win._canvas, "red")
        self._wall_smasher_r(nextCell[1], nextCell[2])
'''
        

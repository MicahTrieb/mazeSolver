from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):

        self.__root = Tk()
        self.__root.title("Title")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
        print("Closed")
    def close(self):
        self.__running = False

    def draw_line(self, line, color):
        line.draw(color, self.__canvas)
    def draw_cell(self, cell, color):
        cell.draw(self.__canvas, color)
    def move_cell(self, cellOne, cellTwo):
        cellOne.draw_move(cellTwo, self.__canvas)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, color, canvas):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill = color, width = 2
        )

class Cell:
    def __init__(self, win, x1, x2, y1, y2, leftWall = True, rightWall = True, topWall = True, bottomWall = True):
        self.leftWall = leftWall
        self.rightWall = rightWall
        self.topWall = topWall
        self.bottomWall = bottomWall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
    def draw(self, color):
        topLeft = Point(self._x1, self._y1)
        topRight = Point(self._x2, self._y1)
        bottomLeft = Point(self._x1, self._y2)
        bottomRight = Point(self._x2, self._y2)
        if self.leftWall:
            self._win.draw_line(Line(topLeft, bottomLeft))
        if self.rightWall:
            self._win.draw_line(Line(topRight, bottomRight))
        if self.topWall:
            self._win.draw_line(Line(topLeft, topRight))
        if self.bottomWall:
            self._win.draw_line(Line(bottomLeft, bottomRight))
    def draw_move(self, to_cell, undo=False):
        centerOfFirstX = (self._x1 + self._x2) / 2
        centerOfFirstY = (self._y1 + self._y2) / 2
        centerOfSecondX = (to_cell._x1 + to_cell._x2) / 2
        centerOfSecondY = (to_cell._y1 + to_cell._y2) / 2
        centerOfFirst = Point(centerOfFirstX, centerOfFirstY)
        centerOfSecond = Point(centerOfSecondX, centerOfSecondY)
        if undo == False:
            Line(centerOfFirst,centerOfSecond).draw("red", self._win.__canvas)
        else:
            Line(centerOfFirst,centerOfSecond).draw("gray", self._win.__canvas)
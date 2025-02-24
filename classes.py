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
    def draw(self, canvas, color):
        topLeft = Point(self._x1, self._y1)
        topRight = Point(self._x2, self._y1)
        bottomLeft = Point(self._x1, self._y2)
        bottomRight = Point(self._x2, self._y2)
        if self.leftWall:
            Line(topLeft, bottomLeft).draw(color, canvas)
        if self.rightWall:
            Line(topRight, bottomRight).draw(color, canvas)
        if self.topWall:
            Line(topLeft, topRight).draw(color, canvas)
        if self.bottomWall:
            Line(bottomLeft, bottomRight).draw(color, canvas)
        pass
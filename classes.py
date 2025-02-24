from tkinter import Tk, BOTH, Canvas
from pointClass import Point, Line

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
    def __init__(self, x, y):
        self.leftWall = True
        self.rightWall = True
        self.topWall = True
        self.bottomWall = True
        self._x1 =
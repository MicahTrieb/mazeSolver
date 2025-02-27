from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self._canvas = Canvas(self.__root, height = height, width = width)
        self._canvas.pack()
        self._running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
    def close(self):
        self._running = False
    def draw_line(self, line, color):
        Line.draw(line, self._canvas, color)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, pointOne, pointTwo):
        self.firstPoint = pointOne
        self.secondPoint = pointTwo
    def draw(self, canvas, color):
        canvas.create_line(self.firstPoint.x, self.firstPoint.y, self.secondPoint.x, self.secondPoint.y, fill=color, width=2)


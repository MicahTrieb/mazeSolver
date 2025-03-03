from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self._canvas = Canvas(self.__root, height = height, width = width, bg="white")
        self._canvas.pack()
        self._running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
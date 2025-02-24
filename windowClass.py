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

    def draw_line(self, Line, color):
        self.draw(Line,color, self.__canvas)
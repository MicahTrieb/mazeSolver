from windowClasses import *
from cellClass import *
from mazeClass import Maze
from time import time
def main():
    window = Window(800,600)
    #window.draw_line(Line(Point(5,5),Point(250,250)), "pink")
    Maze(10, 10, 50, 50, 100, 100, window)
    #newMaze._create_cells()
    window.wait_for_close() 




if __name__ == "__main__":
    main()
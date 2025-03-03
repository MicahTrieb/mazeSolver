from windowClasses import *
from cellClass import *
from mazeClass import Maze
import time
import random
def main():
    #random.seed(None)
    #print (random.randint(1,2))
    window = Window(800,600)
    #window.draw_line(Line(Point(5,5),Point(250,250)), "black")
    Maze(10, 10, 50, 50, 100, 100, window)
    window.wait_for_close()




if __name__ == "__main__":
    main()
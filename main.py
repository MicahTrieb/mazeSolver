from windowClasses import *
from cellClass import *
def main():
    window = Window(800,600)
    window.draw_line(Line(Point(5,5),Point(250,250)), "pink")
    newCell = Cell(25,100,40,160, win=window)
    newCell.draw(newCell.x1,newCell.y1,newCell.x2, newCell.y2, window._canvas, "red")
    window.wait_for_close() 




if __name__ == "__main__":
    main()
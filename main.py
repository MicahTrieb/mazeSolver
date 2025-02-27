from windowClasses import *
from cellClass import *
def main():
    window = Window(800,600)
    window.draw_line(Line(Point(5,5),Point(250,250)), "pink")
    newCell = Cell(25,100,40,160, window)
    newCell.draw(newCell.x1,newCell.y1,newCell.x2, newCell.y2, window._canvas, "red")
    newCell2 = Cell(250, 350, 290, 380, window)
    newCell2.draw(newCell2.x1, newCell2.y1, newCell2.x2, newCell2.y2, window._canvas, "blue")
    newCell.draw_move(newCell2)
    window.wait_for_close() 




if __name__ == "__main__":
    main()
from classes import *

if __name__ == "__main__":
    def main():
        win = Window(800, 600)
        #win.draw_line(Line(Point(5,5), Point(250,250)), "black")
        #(self, x1, x2, y1, y2, win, leftWall = True, rightWall = True, topWall = True, bottomWall = True):
        tempCell = Cell(win, 10, 120, 10, 120, True, True, False, True)
        tempCell2 = Cell(win, 250, 500, 250, 500, True, True, False, True)
        win.draw_cell(tempCell, "blue")
        win.draw_cell(tempCell2, "purple")
        win.move_cell(tempCell, tempCell2)
        win.wait_for_close()

main()
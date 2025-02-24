from classes import *

if __name__ == "__main__":
    def main():
        win = Window(800, 600)
        win.draw_line(Line(Point(5,5), Point(250,250)), "black")
        #(self, x1, x2, y1, y2, win, leftWall = True, rightWall = True, topWall = True, bottomWall = True):
        tempCell = Cell(10, 60, 10, 60, win, True, False, True, True)
        win.draw_cell(tempCell, "blue")
        win.wait_for_close()

main()
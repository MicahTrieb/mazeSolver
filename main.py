from windowClass import *

if __name__ == "__main__":
    def main():
        win = Window(800, 600)
        win.draw_line(Line(Point(5,5), Point(250,250)), "black")
        win.wait_for_close()

main()
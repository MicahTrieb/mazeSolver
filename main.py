from windowClass import *

if __name__ == "__main__":
    def main():
        win = Window(800, 600)
        Window.draw_line(Line(Point(5,5), Point(250,250)))
        win.wait_for_close()

main()
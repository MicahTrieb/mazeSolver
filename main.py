from windowClasses import *
def main():
    window = Window(800,600)
    window.draw(Line(Point(5,5),Point(250,250)), "pink")
    window.wait_for_close() 




if __name__ == "__main__":
    main()
from classes import *
from mazeClass import Maze
if __name__ == "__main__":
    def main():
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        m1._create_cells
        
        win.wait_for_close()

main()
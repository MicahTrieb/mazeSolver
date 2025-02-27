from mazeClass import Maze
import unittest
from classes import *
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        m1._create_cells

if __name__ == "__main__":
    unittest.main()

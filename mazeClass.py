from classes import *
import time
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        
    def _create_cells(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(row, col)
    def _draw_cell(self, row, col):
        print("Drawing")
        topLeft = Point(row * self._cell_size_x,col * self._cell_size_y)
        topRight = Point((row + 1) * self._cell_size_x,col * self._cell_size_y)
        botLeft = Point(row * self._cell_size_x,(col + 1) * self._cell_size_y)
        botRight = Point((row + 1) * self._cell_size_x,(col + 1) * self._cell_size_y)
        fullCell = Cell(self._win, topLeft, topRight, botLeft, botRight)
        fullCell.draw(self._win.__canvas, "pink")
        self._animate()
    def _animate(self):
        self.redraw()
        time.sleep(0.05)

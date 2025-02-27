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
        for col in range(0, self._num_cols):
            self._cells.append([])
            for row in range(0, self._num_rows):
                self._cells[col].append(row)
    def _draw_cell(self, row, col):
        topLeft = Point(row * self._cell_size_x)
        topRight = Point((row + 1) * self._cell_size_x)
        botLeft = Point(col * self._cell_size_y)
        botRight = Point((col + 1) * self._cell_size_y)
        fullCell = Cell(self._win, topLeft, topRight, botLeft, botRight)
        fullCell.draw(self._win.__canvas, "pink")
        self._win.redraw()
        time.sleep(5)

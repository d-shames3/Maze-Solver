from window import Window
from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            seed=None,
            win: Window=None,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        if seed is not None:
            random.seed(seed)
        self.win = win
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self): 
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                cell = Cell(
                        self.x1 + (i * self.cell_size_x),
                        self.x1 + (i * self.cell_size_x) + self.cell_size_x,
                        self.y1 + (j * self.cell_size_y),
                        self.y1 + (j * self.cell_size_y) + self.cell_size_y,
                        self.win
                    )
                col.append(cell)
            self._cells.append(col)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                if self.win is not None:
                    self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        if self.win is not None:
            self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        if self.win is not None:
            self._draw_cell(-1, -1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            coordinates = []

            if i > 0 and not self._cells[i - 1][j]._visited:
                coordinates.append((i - 1, j))
            if i < self.num_cols - 1 and not self._cells[i + 1][j]._visited:
                coordinates.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1]._visited:
                coordinates.append((i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1]._visited:
                coordinates.append((i, j + 1))

            if len(coordinates) == 0:
                if self.win is not None:
                    self._draw_cell(i, j)
                return

            direction_index = random.randrange(len(coordinates))
            next_index = coordinates[direction_index]

            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell._visited = False

from window import Window
from cell import Cell
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
            win: Window=None,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self.win = win
        self._create_cells()
        self._break_entrance_and_exit()

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
        self._break_entrance_and_exit()


    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)

from graphics import Cell
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
        win = None,
        seed = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        if seed is not None:
            random.seed(seed)

        if self.num_rows == 0 or self.num_cols == 0:
            self.valid = False
            return None

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        print("Start creating cells")

        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

        print("Finished creating cells")

    def _draw_cell(self, i, j):
        if self.win is None:
            return

        cell_x1 = self.x1 + i * self.cell_size_x
        cell_y1 = self.y1 + j * self.cell_size_y
        cell_x2 = cell_x1 + self.cell_size_x
        cell_y2 = cell_y1 + self.cell_size_y

        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        
        self.win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        print("Create entry and exit ...")
        self._cells[0][0].has_top_wall = False
        print(self._cells[0][0].has_top_wall)
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
        print("Finished entry and exit.")

    def break_walls_r(self, i, j):
        print(f"Enter Cell {i}, {j}")
        self._cells[i][j].visited = True

        while True:
            cells_to_visit = []

            if (i - 1) in list(range(self.num_cols)):
                if not self._cells[i-1][j].visited:
                    print("Left direction available")
                    cells_to_visit.append((i - 1, j))

            if (i + 1) in list(range(self.num_cols)):
                if not self._cells[i+1][j].visited:
                    print("Right direction available")
                    cells_to_visit.append((i + 1, j))

            if (j - 1) in list(range(self.num_rows)):
                if not self._cells[i][j-1].visited:
                    print("Up direction available")
                    cells_to_visit.append((i, j - 1))

            if (j + 1) in list(range(self.num_rows)):
                if not self._cells[i][j+1].visited:
                    print("Down direction available")
                    cells_to_visit.append((i, j + 1))

            print(cells_to_visit)

            if not cells_to_visit:
                self._draw_cell(i, j)
                return

            i_next, j_next = random.choice(cells_to_visit)
            print(f"Knock down walls to Cell {i_next}, {j_next}")
            if i_next < i:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            elif i_next > i:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if j_next < j:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            elif j_next > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False

            self.break_walls_r(i_next, j_next)

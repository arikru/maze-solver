from graphics import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        self._create_cells()

    def _create_cells(self):
        # fill a self._cells list with lists of cells. Each top-level list is a column of Cell objects; call its _draw_cell() method on each Cell
        self._cells = []

        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cells(i, j)


    def _draw_cells(self, i, j):
        # This method should calculate the x/y position of the Cell based on i, j, the cell_size, and the x/y position of the Maze itself.
        # Once that's calculated, it should draw the cell and call the maze's _animate() method
       pass 

    def _animate(self):
        # simply call the window's redraw() method, then sleep for a short amount of time, e.g. 0.05 seconds.
        pass

import unittest
from maze import Maze
import time

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_create_cells_null(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(
            m1.valid,
            False,
        )

    def test_entrance_wall_broken(self):
        m1 = Maze(0, 0, 10, 10, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
    def test_reset_visited_first_cell(self):
        m1 = Maze(0, 0, 10, 16, 10, 10)
        self.assertEqual(
            m1._cells[0][0].visited,
            False
        )

    def test_reset_visited_last_cell(self):
        m1 = Maze(0, 0, 10, 16, 10, 10)
        self.assertEqual(
            m1._cells[m1.num_cols-1][m1.num_rows-1].visited,
            False
        )

    def test__solve_r_end(self):
        m1 = Maze(0, 0, 10, 16, 10, 10)
        self.assertEqual(
            m1._solve_r(15,9),
            True
        )

if __name__ == "__main__":
    unittest.main()

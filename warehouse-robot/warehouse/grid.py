import numpy as np


class WarehouseGrid:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=np.int8)

    def add_shelf(self, start_row, start_col, height, width):

        self.grid[
            start_row:start_row + height,
            start_col:start_col + width
        ] = 1

    def display(self):
        print(self.grid)
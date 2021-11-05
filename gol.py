import tkinter
import math
import os
import itertools

term_size = os.get_terminal_size()

term_size_cols, term_size_rows = term_size.columns, term_size.lines

class Grid:
    def __init__(self, num_rows: int, num_cols: int, init_state:dict = None):
        self.num_rows = num_rows
        self.num_cols = num_cols

        self.coords = list(itertools.product(range(num_rows), range(num_cols)))

        # `state` will hold the current state of the grid, i.e. a record of
        # which cells are alive and which are dead.
        grid_coords = list(itertools.product(range(num_rows), range(num_rows)))
        self.state = dict.fromkeys(grid_coords, 0)

        # Update grid with initial state
        if init_state:
            self.state.update(init_state)

        # self.__repr__ = self.show_grid()

    # Make list of "relative neighbor coordinates"; e.g., (-1, 1), (-1, 0), etc.
    rel_coords = list(itertools.product((-1, 0, 1), (-1, 0, 1)))
    rel_coords.remove((0,0)) # Remove cell "self" relative coordinates

    # Get neighbor coordinates using relative coordinates
    def get_neighbor(self, cell_coords, rel_coords):
        return (cell_coords[0] + rel_coords[0], cell_coords[1] + rel_coords[1])

    def live_neighbors_count(self, cell: tuple, state) -> list:
        '''
        @param cell: coordinates of cell in grid
        @param state: self.state
        @param rel_coords: relative neighboring coordinates

        Checks states (alive or dead) of neighbors.

        Returns int `count` equal to number of live neighbors
        '''
        return sum([state[self.get_neighbor(cell, rel_c)] for rel_c in self.rel_coords \
                if cell[0] + rel_c[0] >= 0 and \
                   cell[0] + rel_c[0] <= self.num_rows - 1 and \
                   cell[1] + rel_c[1] >= 0 and \
                   cell[1] + rel_c[1] <= self.num_cols - 1])

    def apply_rules(self) -> dict:
        '''
        Since in the GoL the rules are applied to all cells "simultaneously",
        we must record the cell state updates in a separate dictionary and
        then update the grid.
        '''
        g = {}
        for cell, state in self.state.items():
            num_live_neighbors = self.live_neighbors_count(cell, self.state)
            if self.state[cell] == 1 and (num_live_neighbors < 2 or num_live_neighbors > 3):
                g.update({cell: 0})
            elif num_live_neighbors == 3:
                g.update({cell: 1})
        self.state.update(g)

    def show_grid(self):
        for n in self.num_rows:
            pass

# def exit_on_q(key):
#     if key in ('q', 'Q'):
#         raise urwid.ExitMainLoop()

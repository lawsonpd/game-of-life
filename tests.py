import unittest
import itertools

from gol import Grid

class GridState(unittest.TestCase):

    def test_null_transition(self):
        grid = Grid(10, 10) # No initial state
        grid.apply_rules()

        # Expected state (empty)
        control_grid_coords = list(itertools.product(range(10), range(10)))
        control_grid_state = dict.fromkeys(control_grid_coords, 0)

        self.assertEqual(grid.state, control_grid_state)

    def test_cell_reproduction(self):
        init_state = {(8,6): 1, (8,8): 1, (6,8): 1}
        grid = Grid(10, 10, init_state)

        # Applying rules should turn on (bring "alive") (7,7) and turn off (kill)
        # the cells initiated in `init_state`.
        grid.apply_rules()

        # Expected state
        control_grid_coords = list(itertools.product(range(10), range(10)))
        control_grid_state = dict.fromkeys(control_grid_coords, 0)
        control_grid_state.update({(7,7): 1})

        self.assertEqual(grid.state, control_grid_state)

if __name__ == '__main__':
    unittest.main()

import unittest
from gamegrid import GameGrid


class TestGameGrid(unittest.TestCase):
    def setUp(self):
        self.gamegrid = GameGrid(10, 0)

    def test_number_of_rows_and_colums_in_grid_ok(self):
        self.assertEqual(len(self.gamegrid.grid), 10)
        self.assertEqual(len(self.gamegrid.grid[0]), 10)

    def test_mouse_left_click_value_grows(self):
        self.gamegrid.handle_left_mouse((0, 0), 30)
        self.assertEqual(self.gamegrid.grid[0][0], 0)
        self.assertEqual(self.gamegrid.klicked, 0)
        self.gamegrid.handle_left_mouse((0, 90), 30)
        self.assertEqual(self.gamegrid.grid[0][0], 20)
        self.assertEqual(self.gamegrid.klicked, 100)

    def test_mouse_left_click_mine_works(self):
        self.gamegrid2 = GameGrid(10, 100)
        self.gamegrid2.handle_left_mouse((0, 90), 30)
        self.assertTrue(self.gamegrid2.mine_hit)
        self.assertEqual(self.gamegrid2.grid[0][0], 30)

    def test_mouse_right_click_flag(self):
        self.gamegrid.handle_right_mouse((0, 90), 30)
        self.assertEqual(self.gamegrid.grid[0][0], 50)
        self.assertEqual(self.gamegrid.flags, 1)
        self.gamegrid.handle_right_mouse((0, 90), 30)
        self.assertEqual(self.gamegrid.grid[0][0], 0)
        self.assertEqual(self.gamegrid.flags, 0)

    def test_list_neigbours_return_corner_ok(self):
        lista = self.gamegrid.list_neighbours(0, 0)
        self.assertEqual(lista, [(0, 0), (0, 1), (1, 0), (1, 1)])
        lista = self.gamegrid.list_neighbours(9, 9)
        self.assertEqual(lista, [(8, 8), (8, 9), (9, 8), (9, 9)])

    def test_set_numbers_adds_ok(self):
        self.gamegrid.set_numbers(0, 0)
        self.assertEqual(self.gamegrid.grid[0][1], 1)

import unittest
from gamegrid import GameGrid

class TestGameGrid(unittest.TestCase):
    def setUp(self):
        self.gamegrid = GameGrid(10,10)
    
    def test_number_of_rows_and_colums_in_grid_ok(self):
        self.assertEqual(len(self.gamegrid.grid), 10) 
        self.assertEqual(len(self.gamegrid.grid[0]), 10) 

     
    



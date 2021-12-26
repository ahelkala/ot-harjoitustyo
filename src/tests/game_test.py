import unittest
from game import Game
from database import DataBaseConnection


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(10)
    
    def test_blocklist_loaded_ok(self):
        self.assertEqual(len(self.game.block_list), 12)

    def test_game_won_time_ok(self):
        self.game.won = False
        self.game.start_time = 0
        self.game.score_base = DataBaseConnection()
        self.game.check_if_won()
        self.assertEqual(self.game.won_time, "xxx")
        self.game.grid.klicked = self.game.row_count **2 -self.game.mine_count
        self.game.check_if_won()
        self.assertNotEqual(self.game.won_time, "xxx")

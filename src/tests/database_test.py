import unittest
from database import DataBaseConnection


class TestDataBaseConnection(unittest.TestCase):
    def setUp(self):
        self.database = DataBaseConnection()

    def test_database_has_right_number_of_scores(self):
        scores = self.database.get_score()
        self.assertEqual(len(scores), 5)
        self.database = DataBaseConnection()
        scores = self.database.get_score()
        self.assertEqual(len(scores), 5)

    def test_database_adds_score(self):    
        self.database.add_score(0)
        scores = self.database.get_score()
        self.assertEqual(scores[0][1], 0)
import sqlite3
import getpass


class DataBaseConnection:
    def __init__(self):
        self.fail = False
        try:
            self.db = sqlite3.connect("score.db")
        except:
            self.fail = True
        self.db.isolation_level = None
        self.create_score_table = "CREATE TABLE IF NOT EXISTS Scores (id INTEGER PRIMARY KEY, name TEXT, points INTEGER)"
        if not self.fail:
            self.create_tables()

    def create_tables(self):
        try:
            self.db.execute(self.create_score_table)
            score_list = self.get_score()
            if len(score_list) < 5:
                for i in range(5):
                    player = "Player" + str(i+1)
                    score = 9999 - i
                    self.db.execute(
                        "INSERT INTO Scores (name, points) VALUES (?,?)", [player, score])
        except:
            self.fail = True

    def add_score(self, score=999):
        user = getpass.getuser()
        if len(user) > 10:
            user = user[:9]
        if not self.fail:
            self.db.execute(
                "INSERT INTO Scores (name, points) VALUES (?,?)", [user, score])

    def get_score(self):
        top_score = self.db.execute(
            "SELECT name, points FROM Scores ORDER BY points LIMIT 5").fetchall()
        return top_score


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
        except:
            self.fail = True

    def add_score(self, score=999):
        user = getpass.getuser()
        self.db.execute("INSERT INTO Scores (name, points) VALUES (?,?)", [user, score])

    def get_score(self):
        top_score = self.db.execute("SELECT name, points FROM Scores ORDER BY points LIMIT 5").fetchall()
        return top_score

if __name__ == "__main__":
    kanta = DataBaseConnection()
    kanta.add_score(60)
    print(kanta.get_score())

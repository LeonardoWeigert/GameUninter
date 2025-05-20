import sqlite3


class Proxy:

    def __init__(self, db_connection_name: str):
        self.db_name = db_connection_name
        self.connectionDB = sqlite3.connect(db_connection_name)
        self.connectionDB.execute('''
                                   CREATE TABLE IF NOT EXISTS PlayerScore(
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   NamePlayer VARCHAR(10) NOT NULL,
                                   ScorePlayer INTEGER NOT NULL,
                                   DateGame TEXT(30) NOT NULL)
                                '''
                                )

    def insert(self, score_dict: dict):
        self.connectionDB.execute('INSERT INTO PlayerScore (NamePlayer, ScorePlayer, DateGame) VALUES (:NamePlayer, :ScorePlayer, :DateGame)', score_dict)
        self.connectionDB.commit()

    def select(self) -> list:
        return self.connectionDB.execute('SELECT * FROM PlayerScore ORDER BY ScorePlayer DESC LIMIT 5').fetchall()

    def close_db(self):
        return self.connectionDB.close()

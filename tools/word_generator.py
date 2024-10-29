import random
import sqlite3

class Word:
    def __init__(self):
        with sqlite3.connect("databases/words.sql") as database:
            cursor = database.cursor()
            self.words: list[tuple[str]] = cursor.execute("SELECT * FROM Words").fetchall()

    def get(self) -> str:
        return random.choice(self.words)[0]

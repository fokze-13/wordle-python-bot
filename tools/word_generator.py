import random
import sqlite3
from configs.config import load

config = load()

class Word:
    def __init__(self):
        with sqlite3.connect(config.words_database_path) as database:
            cursor = database.cursor()
            self.words: list[tuple[str]] = cursor.execute("SELECT * FROM Words").fetchall()

    def get(self) -> str:
        return random.choice(self.words)[0]

import sqlite3
from datetime import datetime
from configs.config import load

config = load()

class User:
    def __init__(self, user_id: int):
        self.user_id = user_id

    def new_user(self):
        with sqlite3.connect(config.user_database_path) as database:
            cursor = database.cursor()
            if not (cursor.execute("SELECT * FROM Users WHERE id = ?", [self.user_id]).fetchone()):
                cursor.execute("INSERT INTO Users(id, last_day, last_month, last_year, wins, total_games) VALUES (?, ?, ?, ?, ?, ?)", [self.user_id, 0, 0, 0, 1, 1])

    def get_win(self):
        with sqlite3.connect(config.user_database_path) as database:
            cursor = database.cursor()
            return cursor.execute("SELECT wins FROM Users WHERE id = ?", [self.user_id]).fetchone()[0]

    def get_total_games(self):
        with sqlite3.connect(config.user_database_path) as database:
            cursor = database.cursor()
            return cursor.execute("SELECT total_games FROM Users WHERE id = ?", [self.user_id]).fetchone()[0]

    def set_win(self):
        with sqlite3.connect(config.user_database_path) as database:
            cursor = database.cursor()
            wins, total_games = cursor.execute("SELECT wins, total_games FROM Users WHERE id = ?", [self.user_id]).fetchone()
            cursor.execute("UPDATE Users SET wins = ?, total_games = ? WHERE id = ?", [wins+1, total_games+1, self.user_id])

    def set_lose(self):
        with sqlite3.connect(config.user_database_path) as database:
            cursor = database.cursor()
            total_games = cursor.execute("SELECT total_games FROM Users WHERE id = ?", [self.user_id]).fetchone()[0]
            cursor.execute("UPDATE Users SET total_games = ? WHERE id = ?", [total_games+1, self.user_id])

    def get_last_game(self) -> tuple[int, int, int]:
        with sqlite3.connect(config.user_database_path) as database:
            cursor = database.cursor()
            return cursor.execute("SELECT last_day, last_month, last_year FROM Users WHERE id = ?", [self.user_id]).fetchone()

    def set_last_game(self, date: tuple[int, int, int]):
        with sqlite3.connect(config.user_database_path) as database:
            cursor = database.cursor()
            cursor.execute("UPDATE Users SET last_day = ?, last_month = ?, last_year = ? WHERE id = ?", [*date, self.user_id])

import sqlite3
from datetime import datetime

PATH = "databases/users.sql" #TODO path to .env

def new_user(user_id: int):
    with sqlite3.connect(PATH) as database:
        cursor = database.cursor()
        if not (cursor.execute("SELECT * FROM Users WHERE id = ?", [user_id]).fetchone()):
            cursor.execute("INSERT INTO Users(id, last_day, last_month, last_year) VALUES (?, ?, ?, ?)", [user_id, 0, 0, 0])


class LastGame:
    @classmethod
    def get(cls, user_id: int) -> tuple[int, int, int]:
        with sqlite3.connect(PATH) as database:
            cursor = database.cursor()
            return cursor.execute("SELECT last_day, last_month, last_year FROM Users WHERE id = ?", [user_id]).fetchone()

    @classmethod
    def set(cls, user_id: int, date: tuple[int, int, int]):
        with sqlite3.connect(PATH) as database:
            cursor = database.cursor()
            cursor.execute("UPDATE Users SET last_day = ?, last_month = ?, last_year = ? WHERE id = ?", [*date, user_id])

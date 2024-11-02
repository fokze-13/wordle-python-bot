from tools.word_generator import Word
from datetime import datetime

class WordOfDay:
    def __init__(self):
        self.database = Word()
        self.word = self.database.get()
        self.today = datetime.today().day, datetime.today().month, datetime.today().year

    def get(self):
        if self.today != (datetime.today().day, datetime.today().month, datetime.today().year):
            self.word = self.database.get()
        return self.word

    @staticmethod
    def time_left():
        return f"{24-datetime.today().hour}:{60-datetime.today().minute}:{60-datetime.today().second}"

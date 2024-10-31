from tools.word_generator import Word
from datetime import datetime

class WordOfDay:
    def __init__(self):
        self.database = Word()
        self.word = self.database.get()
        self.today = datetime.today().day, datetime.today().month, datetime.today().year

    def get(self):
        if self.today == (datetime.today().day, datetime.today().month, datetime.today().year):
            return self.word
        self.word = self.database.get()
        return self.word

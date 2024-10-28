from aiogram.filters import BaseFilter
from aiogram.types import Message

class ValidWordFilter(BaseFilter):
    async def __call__(self, message: Message):
        return len(message.text) == 5

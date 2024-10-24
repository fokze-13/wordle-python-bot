from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from lexicons.lexicon_ru import command_answers

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(command_answers["start"])


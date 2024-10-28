from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from lexicons.lexicon_ru import command_answers
from keyboards.inline_keyboards import game_keyboard
from aiogram import F

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(command_answers["start"])

@router.message(Command("help"))
async def help(message: Message):
    await message.answer(command_answers["help"])

@router.message(Command("game"))
async def game(message: Message):
    await message.answer(command_answers["game"], reply_markup=game_keyboard)

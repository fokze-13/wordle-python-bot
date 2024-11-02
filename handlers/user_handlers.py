from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from lexicons.lexicon_ru import command_answers, default_answer
from keyboards.inline_keyboards import game_keyboard
from aiogram.fsm.context import FSMContext
from tools.user_info import User
from aiogram import F

router = Router()

@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    user = User(message.from_user.id)
    user.new_user()
    await state.clear()
    await message.answer(command_answers["start"])

@router.message(Command("help"))
async def help(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(command_answers["help"])

@router.message(Command("game"))
async def game(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(command_answers["game"], reply_markup=game_keyboard)

@router.message(Command("stats"))
async def stats(message: Message, state: FSMContext):
    await state.clear()
    user = User(message.from_user.id)
    await message.answer(command_answers["stats"].format(total_games=user.get_total_games(),
                                                         wins=user.get_win(),
                                                         loses=user.get_total_games()-user.get_win(),
                                                         winrate=round(user.get_win()/user.get_total_games(), 2)))

@router.message(F.text)
async def default(message: Message):
    await message.answer(default_answer)

from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import F
from keyboards.inline_keyboards import start_daily_game_keyboard, start_regular_game_keyboard, game_keyboard
from lexicons.lexicon_ru import game_start_confirmation, has_played_daily_game, has_pressed_button
from tools.user_info import User
from datetime import datetime
from tools.word_of_day import WordOfDay

router = Router()

@router.callback_query(F.data == "daily_mode")
async def daily_mode_callback(callback: CallbackQuery):
    user = User(callback.from_user.id)
    try:
        if user.get_last_game() == (datetime.today().day, datetime.today().month, datetime.today().year):
            await callback.message.edit_text(has_played_daily_game.format(time=WordOfDay.time_left()), reply_markup=game_keyboard)
        else:
            await callback.message.edit_text(game_start_confirmation, reply_markup=start_daily_game_keyboard)
    except:
        await callback.answer(has_pressed_button)

@router.callback_query(F.data == "regular_mode")
async def regular_mode_callback(callback: CallbackQuery):
    try:
        await callback.message.edit_text(game_start_confirmation, reply_markup=start_regular_game_keyboard)
    except:
        await callback.answer(has_pressed_button)

from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import F
from keyboards.inline_keyboards import start_daily_game_keyboard, start_regular_game_keyboard
from lexicons.lexicon_ru import game_start_confirmation

router = Router()

@router.callback_query(F.data == "daily_mode")
async def daily_mode_callback(callback: CallbackQuery):
    await callback.message.edit_text(game_start_confirmation, reply_markup=start_daily_game_keyboard)
    await callback.answer()

@router.callback_query(F.data == "regular_mode")
async def regular_mode_callback(callback: CallbackQuery):
    await callback.message.edit_text(game_start_confirmation, reply_markup=start_regular_game_keyboard)
    await callback.answer()
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import F
from keyboards.inline_keyboards import start_game_keyboard

router = Router()

@router.callback_query(F.data == "daily_mode")
async def daily_mode_callback(callback: CallbackQuery):
    await callback.message.answer("В разработке") #TODO
    await callback.answer()

@router.callback_query(F.data == "regular_mode")
async def regular_mode_callback(callback: CallbackQuery):
    await callback.message.edit_text("ОК, жми начать", reply_markup=start_game_keyboard) #TODO
    await callback.answer()
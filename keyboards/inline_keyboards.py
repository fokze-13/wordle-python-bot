from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from lexicons.lexicon_ru import inline_keyboard_buttons

gk_daily_mode = InlineKeyboardButton(text=inline_keyboard_buttons["daily_mode"], callback_data="daily_mode")
gk_regular_mode = InlineKeyboardButton(text=inline_keyboard_buttons["regular_mode"], callback_data="regular_mode")
game_keyboard = InlineKeyboardMarkup(inline_keyboard=[[gk_daily_mode, gk_regular_mode]])

start_game_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Начать", callback_data="game")]]) #TODO
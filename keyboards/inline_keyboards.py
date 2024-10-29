from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from lexicons.lexicon_ru import inline_keyboard_buttons, start_game_button, replay_game_choice

gk_daily_mode = InlineKeyboardButton(text=inline_keyboard_buttons["daily_mode"], callback_data="daily_mode")
gk_regular_mode = InlineKeyboardButton(text=inline_keyboard_buttons["regular_mode"], callback_data="regular_mode")
game_keyboard = InlineKeyboardMarkup(inline_keyboard=[[gk_daily_mode, gk_regular_mode]])

start_daily_game_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=start_game_button, callback_data="daily_game")]])
start_regular_game_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=start_game_button, callback_data="regular_game")]])

rgk_yes = InlineKeyboardButton(text=replay_game_choice["yes"], callback_data="replay_yes")
rgk_no = InlineKeyboardButton(text=replay_game_choice["no"], callback_data="replay_no")
replay_game_keyboard = InlineKeyboardMarkup(inline_keyboard=[[rgk_yes], [rgk_no]])
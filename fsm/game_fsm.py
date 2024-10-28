from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
#from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import Message, CallbackQuery
from filters.game_filters import ValidWordFilter
from aiogram import F
from aiogram.filters import Command

router = Router()

class GameFSM(StatesGroup):
    guessing = State()

'''
TODO every state, and remake text message handler
'''

@router.callback_query(F.data == "game")
async def start_game(callback: CallbackQuery, state: FSMContext):
    await state.set_state(GameFSM.guessing)
    await callback.message.answer("guess the word")
    await callback.answer()

@router.message(GameFSM.guessing, ValidWordFilter(), F.text.lower() == "penis")
async def process_guessing_is_correct(message: Message, state: FSMContext):
    await message.answer("correct")
    await state.clear()

@router.message(GameFSM.guessing, ValidWordFilter())
async def process_guessing_is_incorrect(message: Message, state: FSMContext):
    await message.answer("incorrect, try one more")
    await state.set_state(GameFSM.guessing)

@router.message(GameFSM.guessing)
async def process_guessing_is_not_valid(message: Message, state: FSMContext):
    await message.answer("not valid, try one more")
    await state.set_state(GameFSM.guessing)

@router.message(GameFSM, Command("cancel"))
async def cancel(message: Message, state: FSMContext):
    await message.answer("canceled")
    await state.clear()

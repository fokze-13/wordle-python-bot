from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from filters.game_filters import ValidWordFilter
from aiogram import F
from aiogram.filters import Command
from lexicons.lexicon_ru import daily_fsm_context_answers

router = Router()
#TODO daily word generator

class DailyGameFSM(StatesGroup):
    guessing = State()


@router.callback_query(F.data == "daily_game")
async def start_game(callback: CallbackQuery, state: FSMContext):
    await state.set_state(DailyGameFSM.guessing)
    await callback.message.answer(daily_fsm_context_answers["guess"])
    await callback.answer()

@router.message(DailyGameFSM.guessing, ValidWordFilter(), F.text.lower() == "penis")
async def process_guessing_is_correct(message: Message, state: FSMContext):
    await message.answer(daily_fsm_context_answers["correct"])
    await state.clear()

@router.message(DailyGameFSM.guessing, ValidWordFilter())
async def process_guessing_is_incorrect(message: Message, state: FSMContext):
    await message.answer(daily_fsm_context_answers["incorrect"])
    await state.set_state(DailyGameFSM.guessing)

@router.message(DailyGameFSM.guessing)
async def process_guessing_is_not_valid(message: Message, state: FSMContext):
    await message.answer(daily_fsm_context_answers["not_valid"])
    await state.set_state(DailyGameFSM.guessing)

@router.message(DailyGameFSM.guessing, Command("stop"))
async def cancel(message: Message, state: FSMContext):
    await message.answer(daily_fsm_context_answers["stop"])
    await state.clear()

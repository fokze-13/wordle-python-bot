from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from filters.game_filters import ValidWordFilter
from aiogram import F
from aiogram.filters import Command
from keyboards.inline_keyboards import replay_game_keyboard
from lexicons.lexicon_ru import regular_fsm_context_answers
from tools.word_generator import Word

router = Router()
word_generator = Word()

class RegularGameFSM(StatesGroup):
    guessing = State()
    replay = State()

@router.callback_query(F.data == "regular_game")
async def start_game(callback: CallbackQuery, state: FSMContext):
    await state.update_data(word = word_generator.get())
    await state.set_state(RegularGameFSM.guessing)
    await callback.message.answer(regular_fsm_context_answers["guess"])
    await callback.answer()

@router.message(RegularGameFSM.guessing, ValidWordFilter())
async def process_guessing(message: Message, state: FSMContext):
    data = await state.get_data()
    if data["word"] == message.text.lower():
        await message.answer(regular_fsm_context_answers["correct"], reply_markup=replay_game_keyboard)
        await state.set_state(RegularGameFSM.replay)

    await message.answer(regular_fsm_context_answers["incorrect"])
    await state.set_state(RegularGameFSM.guessing)

@router.message(RegularGameFSM.guessing)
async def process_guessing_is_not_valid(message: Message, state: FSMContext):
    await message.answer(regular_fsm_context_answers["not_valid"])
    await state.set_state(RegularGameFSM.guessing)

@router.callback_query(F.data == "replay_yes")
async def process_replay_yes(callback: CallbackQuery, state: FSMContext):
    await state.update_data(word=word_generator.get())
    await callback.message.answer(regular_fsm_context_answers["guess"])
    await state.set_state(RegularGameFSM.guessing)
    await callback.answer()

@router.callback_query(F.data == "replay_no")
async def process_replay_no(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(regular_fsm_context_answers["replay_no"])
    await state.clear()
    await callback.answer()

@router.message(RegularGameFSM.guessing, Command("stop"))
async def cancel(message: Message, state: FSMContext):
    await message.answer(regular_fsm_context_answers["stop"])
    await state.clear()

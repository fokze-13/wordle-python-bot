from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from filters.game_filters import ValidWordFilter
from aiogram import F
from aiogram.filters import Command
from lexicons.lexicon_ru import daily_fsm_context_answers
from tools.word_of_day import WordOfDay
from tools.check_word import check
from tools.user_info import LastGame
from datetime import datetime

router = Router()
word = WordOfDay()
ATTEMPTS = 5

class DailyGameFSM(StatesGroup):
    guessing = State()


@router.callback_query(F.data == "daily_game")
async def start_game(callback: CallbackQuery, state: FSMContext):
    await state.update_data(word=word.get(), attempts=ATTEMPTS)
    await state.set_state(DailyGameFSM.guessing)
    await callback.message.answer(daily_fsm_context_answers["guess"])
    await callback.answer()


@router.message(DailyGameFSM.guessing, ValidWordFilter())
async def process_guessing(message: Message, state: FSMContext):
    data = await state.get_data()
    print(data["word"]) #test

    if data["attempts"] > 0:
        if data["word"] == message.text.lower():
             await message.answer(daily_fsm_context_answers["correct"].format(word=data["word"],
                                                                            check_word=check(message.text.lower(),
                                                                                                 data["word"]),
                                                                            time="time"))
             await state.clear()

        else:
            await state.update_data(attempts=data["attempts"] - 1)
            await message.answer(daily_fsm_context_answers["incorrect"].format(word=message.text,
                                                                                 check_word=check(message.text.lower(),
                                                                                                  data["word"]),
                                                                                 attempts=data["attempts"]))
            await state.set_state(DailyGameFSM.guessing)

    else:
        await message.answer(daily_fsm_context_answers["end"].format(word=data["word"],
                                                                     time="time"))
        await state.clear()
    LastGame.set(message.from_user.id, (datetime.today().day, datetime.today().month, datetime.today().year))


@router.message(DailyGameFSM.guessing)
async def process_guessing_is_not_valid(message: Message, state: FSMContext):
    await message.answer(daily_fsm_context_answers["not_valid"])
    await state.set_state(DailyGameFSM.guessing)


@router.message(DailyGameFSM.guessing, Command("stop"))
async def stop(message: Message, state: FSMContext):
    await message.answer(daily_fsm_context_answers["stop"])
    await state.clear()

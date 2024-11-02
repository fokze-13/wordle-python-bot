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
from tools.check_word import check
from tools.user_info import User

router = Router()
word_generator = Word()
ATTEMPTS = 5

class RegularGameFSM(StatesGroup):
    guessing = State()
    replay = State()


@router.callback_query(F.data == "regular_game")
async def start_game(callback: CallbackQuery, state: FSMContext):
    await state.update_data(word=word_generator.get(), attempts=ATTEMPTS)
    await state.set_state(RegularGameFSM.guessing)
    await callback.message.answer(regular_fsm_context_answers["guess"])
    await callback.answer()


@router.message(RegularGameFSM.guessing, ValidWordFilter())
async def process_guessing(message: Message, state: FSMContext):
    user = User(message.from_user.id)
    data = await state.get_data()

    if data["attempts"] > 0:
        if data["word"] == message.text.lower():
             await message.answer(regular_fsm_context_answers["correct"].format(word=data["word"],
                                                                                check_word=check(message.text.lower(),
                                                                                                 data["word"])),
                                  reply_markup=replay_game_keyboard)
             await state.set_state(RegularGameFSM.replay)
             user.set_win()
        else:
            await state.update_data(attempts=data["attempts"] - 1)
            await message.answer(regular_fsm_context_answers["incorrect"].format(word=message.text,
                                                                                 check_word=check(message.text.lower(),
                                                                                                  data["word"]),
                                                                                 attempts=data["attempts"]))
            await state.set_state(RegularGameFSM.guessing)

    else:
        await message.answer(regular_fsm_context_answers["end"].format(word=data["word"]), reply_markup=replay_game_keyboard)
        await state.set_state(RegularGameFSM.replay)
        user.set_lose()

@router.message(RegularGameFSM.guessing)
async def process_guessing_is_not_valid(message: Message, state: FSMContext):
    await message.answer(regular_fsm_context_answers["not_valid"])
    await state.set_state(RegularGameFSM.guessing)


@router.callback_query(RegularGameFSM.replay, F.data == "replay_yes")
async def process_replay_yes(callback: CallbackQuery, state: FSMContext):
    await state.update_data(word=word_generator.get(), attempts=ATTEMPTS)
    await callback.message.answer(regular_fsm_context_answers["guess"])
    await state.set_state(RegularGameFSM.guessing)
    await callback.answer()


@router.callback_query(RegularGameFSM.replay, F.data == "replay_no")
async def process_replay_no(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(regular_fsm_context_answers["replay_no"])
    await state.clear()
    await callback.answer()


@router.message(RegularGameFSM.guessing, Command("stop"))
async def stop(message: Message, state: FSMContext):
    await message.answer(regular_fsm_context_answers["stop"])
    await state.clear()

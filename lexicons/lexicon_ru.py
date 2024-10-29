commands = {"/game": "Начать игру",
            "/help": "Помощь"}

command_answers = {"start": "<b>Привет это игра wordle!</b> \n\n Что-бы начать игру пиши /game\n\n Требуется помощь? /help",
                   "help": f"<b>Вот список доступных команд</b>:\n" + '\n'.join(f"{key}: {value}" for key, value in commands.items()),
                   "game": "<b>Отлично!</b> Выбирай режим"}

inline_keyboard_buttons = {"daily_mode": "Режим Daily",
                           "regular_mode": "Обычный режим"}

game_start_confirmation = "Хорошо! Жми <b>Начать</b>"
start_game_button = "Начать"

daily_fsm_context_answers = {"guess": "<b>Попробуй угадать сегодняшнее слово!</b>\nУ тебя есть 5 попыток",
                             "not_valid": "Ты должен ввести слово из 5 букв!",
                             "incorrect": "Неа, неправильно",
                             "correct": "<b>Правильно!</b> ты угадал сегодняшнее слово: {word}, Теперь возвращайся через {time}",
                             "stop": "Приостановлено, если ты передумал, пиши /game"}

regular_fsm_context_answers = {"guess": "<b>Я загадал слово!</b>\nУгадай его. У тебя есть 5 попыток",
                             "not_valid": "Ты должен ввести слово из 5 букв!",
                             "incorrect": "Неа, неправильно",
                             "correct": "<b>Правильно!</b> ты угадал мое слово, хочешь сыграть еще?",
                             "stop": "Приостановлено, если ты передумал, пиши /game",
                             "replay_no": "<b>Хорошо.</b> Если хочешь поиграть еще, пиши /game"}


replay_game_choice = {"yes": "Да",
                      "no": "Нет"}
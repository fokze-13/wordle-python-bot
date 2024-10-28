commands = {"/game": "Начать игру",
            "/help": "Помощь"}

command_answers = {"start": "<b>Привет это игра wordle!</b> \n\n Что-бы начать игру пиши /game\n\n Требуется помощь? /help",
                   "help": f"<b>Вот список доступных команд</b>:\n" + '\n'.join(f"{key}: {value}" for key, value in commands.items()),
                   "game": "<b>Отлично!</b> Выбирай режим"}

inline_keyboard_buttons = {"daily_mode": "Режим Daily",
                           "regular_mode": "Обычный режим"}

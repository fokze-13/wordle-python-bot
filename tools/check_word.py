CORRECT = "🟩"
IN_WORD = "🟨"
INCORRECT = "⬜"

def check(input_word: str, correct_word: str) -> str:
    list_input_word = input_word
    list_correct_word = correct_word

    result = ""
    for input_letter, correct_letter in zip(list_input_word, list_correct_word):
        if input_letter == correct_letter:
            result += CORRECT
        elif input_letter in list_correct_word:
            result += IN_WORD
        else:
            result += INCORRECT
    return result

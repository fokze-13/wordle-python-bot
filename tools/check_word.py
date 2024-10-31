CORRECT = "🟩"
IN_WORD = "🟨"
INCORRECT = "⬜"

def check(input_word: str, correct_word: str) -> str:
    list_input_word = list(input_word)
    list_correct_word = list(correct_word)

    result = ""
    for i in range(5):
        if list_input_word[i] == list_correct_word[i]:
            result += CORRECT
        elif list_input_word[i] in list_correct_word:
            result += IN_WORD
        else:
            result += INCORRECT
    return result

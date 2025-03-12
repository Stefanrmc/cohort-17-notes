def prompt_user_input_until_word_guessed(word_list: list[str]) -> str:
    """Asks user for input until they guess a word from the list"""

    number_guesses = 0

    guess = None

    while guess not in words:
        guess = input("Please guess a word:")
        number_guesses += 1
        return guess

# No repeated letters, at least six letters long, case-insensitive


def prompt_user_input_until_valid_str_entered() -> str:
    """Prompts user for input until they enter a string with at least six letters, none repeated, case-insensitive"""

    attempt = None

    while len(attempt) < 6:
        attempt = input("Choose an option: ")


def has_spaced_pair(text: str) -> bool:
    """Returns true if a string has one character repeated with two steps in between"""

    for i in range(len(text)):
        if text[i] == text[i+3]:
            if text[i] != text[i+1] and text[i] != text[i+2]:
                return True
        else:
            return False


if __name__ == '__main__':

    print(has_spaced_pair('roar'))

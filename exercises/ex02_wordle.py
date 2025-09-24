"""guess the correct word!"""

__author__: str = "730661317"


def input_guess(expected_length: int) -> str:
    """asks for a guess of expected lendth and returns it"""
    guess = input("Enter a " + str(expected_length) + " character word: ")
    while len(guess) != expected_length:
        guess = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return guess


def contains_char(search_string: str, char: str) -> bool:
    """check if a specific character is in a given str"""
    assert len(char) == 1, f"len('{char}') is not 1"
    i = 0
    while i < len(search_string):
        if search_string[i] == char:
            return True
        i += 1
    return False


WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def emojified(guess: str, secret: str) -> str:
    """creates colored emojis based on if the guess is correct or incorrect"""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    i = 0
    result = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            result = result + GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                result = result + YELLOW_BOX
            else:
                result = result + WHITE_BOX
        i += 1
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop. runs the whole program"""
    turn = 1
    won = False
    while turn <= 6 and not won:
        print("=== Turn " + str(turn) + "/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            print("You won in " + str(turn) + "/6 turns!")
            won = True
        else:
            turn += 1

    if not won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")

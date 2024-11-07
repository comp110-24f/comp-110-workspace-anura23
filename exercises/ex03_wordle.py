"""Coding a structured Wordle game."""

__author__ = "730478902"


def input_guess(secret_word_len: int) -> str:
    """Will ensure user enters guess of correct length"""
    input_word: str = input(f"Enter a {secret_word_len} character word: ")
    # global variable that stores user's word.
    while secret_word_len != len(input_word):
        input_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
        # created a while loop to compare the length of inputted word with set length.
        # If input word has different number of characters, prints error statement.
        # Important to redefine input_word as the new guess if previous guess was wrong.
    return input_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """will test each index of secret_word to see if it matches char_guess."""
    assert len(char_guess) == 1
    index: int = 0  # Set this global variable to iterate over secret_word indices.
    occurrence: int = 0  # keeps track of char_guess matches in secret_word.
    while index < len(secret_word):
        if (
            char_guess == secret_word[index]
        ):  # check each index of secret_word with char_guess.
            occurrence = occurrence + 1  # store matches in occurrence.
        index = (
            index + 1
        )  # index iteration kept outside if statement to occur if while block entered.
    if occurrence > 0:  # defining occurrence serves as conditional for boolean.
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Compare's user guess and secret word to return emojis depicting accuracy."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    result: str = ""  # Initially defines result as an empty string.
    # this allows one to sequentially add emoji blocks to a string (result).
    while index < len(secret):
        if contains_char(secret_word=secret, char_guess=guess[index]):
            # Call contains_char to see if char at certain index in guess is in secret.
            if guess[index] == secret[index]:
                result = (
                    result + GREEN_BOX
                )  # green emoji included if char at some index in guess matches secret.
                # the empty string in result is edited to include a green emoji.
            else:
                result = result + YELLOW_BOX
                # Exact character (char_guess) does not match at this index.
                # char_guess does occur at an index in secret -> yellow emoji is placed.
        else:
            result = (
                result + WHITE_BOX
            )  # this statment is kept outside internal if/else statement.
            # Paired with outer if -> if certain char doesn't occur in secret -> white
        index = (
            index + 1
        )  # ensures that while loop progresses towards conditional returning false.
    return result  # returns sequence of emoji blocks as a string.


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 1  # will iterate what turn a user is on in game.
    user_input: str = (
        ""  # made user_input an empty string -> later defined by calling input_guess.
        # defined user_input here as a global variable
        #  Enables it to serve as an argument in later function calls.
    )
    while turn_number <= 6 and user_input != secret:
        print(f"=== Turn {turn_number}/6 ===")
        user_input = input_guess(
            secret_word_len=len(secret)
        )  # calling input_guess enables user to enter a word of a certain length.
        # will be used for comparison to secret word in later function calls.
        print(
            emojified(guess=user_input, secret=secret)
        )  # calling emojified function based on guessed word relative to secret.
        turn_number += 1
    if user_input == secret:
        print(
            f"You won in {turn_number - 1}/6 turns!"
        )  # have to do turn-1 since while loop would add one to turn_number.
        # subtracting one correct this addition.
    else:
        print("X/6 - Sorry, try again tomorrow!")

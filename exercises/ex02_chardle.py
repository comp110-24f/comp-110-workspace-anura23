"""EX02 - Chardle - A cute step towards Wordle."""

__author__ = "730478902"


def input_word() -> str:
    """Function that stores user input as a string."""
    user_input: str = input("Enter a 5-character word: ")
    if (
        len(user_input) == 5
    ):  # chardle depends on the word being 5 letters long -> subject of conditional.
        print(user_input)
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # exit code here to prevent unneccesary downstream print + return.
        print(user_input)
    return user_input


def input_letter() -> str:
    """Function that prompts user for a character."""
    user_character: str = input("Enter a single character: ")
    if (
        len(user_character) != 1
    ):  # chardle depends on the character being a single letter.
        print("Error: Character must be a single character.")
        exit()  # again, exit code here to prevent redundant downstream print + return.
        print(user_character)
    else:
        print(user_character)
    return user_character


def contains_char(word: str, letter: str) -> None:
    """Function that checks if a letter matches any character in input word."""
    print("Searching for " + letter + " in " + word)
    identical_letter: int = (
        0  # this is the local variable that will iterate the indices and count repeats.
    )
    if (
        word[0] == letter
    ):  # series of if statements to see whether index matches the inputed character.
        print(
            letter + " found at index 0"
        )  # entering the corresponding then block -> prints index the letter resides.
        identical_letter = (
            identical_letter + 1
        )  # sequentially iterates value of identical_letter by 1 if then block entered.
    if word[1] == letter:
        print(letter + " found at index 1")
        identical_letter = identical_letter + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        identical_letter = identical_letter + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        identical_letter = identical_letter + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        identical_letter = identical_letter + 1
    if identical_letter == 0:
        print("No instances of " + letter + " found in " + word)
    if identical_letter == 1:
        print(
            "1 instance of " + letter + " found in " + word
        )  # Created 3 different if statements to achieve singular vs. plural grammar.
    if identical_letter >= 2:
        print(
            str(identical_letter) + " instances of " + letter + " found in " + word
        )  # Had to convert identical_letter to a string to concatenate.


def main() -> None:
    """Will coordinate all function calls and operations."""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":  # enables us to run python program as a module.
    main()

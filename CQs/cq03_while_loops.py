"""Practice with using a while loop to iterate over a string"""

__author__ = "730478902"


def num_instances(phrase: str, search_char: str) -> int:
    """Given string and single character, will yield frequency of character in phrase"""
    count: int = 0  # will check total frequency of search_char in phrase.
    index: int = 0  # Use an index as it allows one to check each letter.
    while index < len(phrase):
        if search_char == phrase[index]:
            count = count + 1
        index = (
            index + 1
        )  # Should be outside the if statement so index is always increased.
    return count

"""Practice writing a function that modifies a list and writing unit tests!"""

__author__ = "730478902"


def find_and_remove_max(input: list[int]) -> int:
    """Finds and returns largest number in list, and removes its occurrence."""
    if len(input) == 0:
        return -1
    index: int = 0
    max_value: int = input[0]
    index_2: int = len(input) - 1
    while index < len(input):
        if input[index] >= max_value:
            max_value = input[index]
        index += 1
    # #while index_2 < len(input):
    #     if input[index_2] == max_value:
    #         input_2.pop(index_2)
    #     input_2 = input
    #

    while index_2 > 0:
        if input[index_2] == max_value:
            input.pop(index_2)
        index_2 -= 1

    return max_value

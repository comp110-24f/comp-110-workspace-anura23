"""Summing the elements of a list using different loops"""

__author__ = "730478902"


def w_sum(vals: list[float]) -> float:
    """Will return the sum of all element in the list with while loop."""
    index: int = 0
    sum: float = 0.0
    while index < len(vals):
        sum = sum + vals[index]
        index += 1
    return sum


def f_sum(vals_1: list[float]) -> float:
    """Returns the sum of all elements in list using for in loop."""
    sum_1: float = 0.0
    for elem in vals_1:
        sum_1 = sum_1 + elem
    return sum_1


def f_range_sum(vals_2: list[float]) -> float:
    """Returns the sum of all elements in list using range."""
    sum_2: float = 0.0
    for index in range(0, len(vals_2)):
        sum_2 = sum_2 + vals_2[index]
    return sum_2

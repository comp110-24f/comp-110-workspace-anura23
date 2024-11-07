"""List Utility Functions Exercise"""

__author__ = "730478902"


def all(listy: list[int], inty: int) -> bool:
    """Function will check if all the ints in the list are same as given int."""
    index: int = 0
    occurrence: int = (
        0  # Defined this global variable to iterate over identical elements.
    )
    while index < len(listy):
        if inty == listy[index]:
            occurrence = (
                occurrence + 1
            )  # Standard while loop setup for iterating over index.
        index = index + 1
    if (
        occurrence == len(listy) and len(listy) != 0
    ):  # Based the bool return on value of occurrence.
        # Also included a condition to ensure that the input list is not empty.
        return True
    else:
        return False


def max(input: list[int]) -> int:
    """When given a list of ints, this function will return the largest number"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")  # this code was provided to us.
    index: int = 0
    max_int: int = input[0]  # setting the initial value of max value to first element.
    while index < len(input):
        if input[index] >= max_int:
            max_int = input[
                index
            ]  # will modify max_int if a successive element is larger than it.
        index = index + 1
    return max_int  # can simply return this max_int global variable.


def is_equal(input_1: list[int], input_2: list[int]) -> bool:
    """Given 2 int lists, function will check if every element at all index is equal."""
    index_1: int = 0
    index_2: int = 0
    equal: int = (
        0  # defined this global variable to bookeep instances of equal elements.
    )
    while (
        index_1 < len(input_1)
        and index_2 < len(input_2)
        and len(input_1)
        == len(input_2)  # must ensure that the length of the two lists is the same.
    ):
        if (
            input_1[index_1] == input_2[index_2]
        ):  # will sequentially check each element at each index.
            equal = (
                equal + 1
            )  # by adding one to equal, we are bookeeping instances of equality.
        index_1 += (
            1  # kept these two index iterations outside then block to always happen.
        )
        index_2 += 1
    if equal == len(input_1) and equal == len(
        input_2
    ):  # if the value of equal is the length of input_1 or input_2
        # then this means that both lists have same elements at same indexes.
        return True
    else:
        return False


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Will mutate first list by appending 2nd list's values to end of it."""
    index_2: int = 0  # I will iterate over the indexes of list_2.
    new_list: list[int] = (
        list_1  # setting up a new list to be modified.
        # initially consists of the elements of list_1, but will be appended.
    )
    while index_2 < len(list_2):
        new_list.append(
            list_2[index_2]
        )  # will continuously append new_list with list_2 elements.
        index_2 += 1
    print(new_list)

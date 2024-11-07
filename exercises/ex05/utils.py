"""Implementing List Utility Functions"""

__author__ = "730478902"


def only_evens(input_list: list[int]) -> list[int]:
    """Returns a new list that only contains even integers present in input."""
    index: int = 0
    even_list: list[int] = []  # created an empty list in globals.
    # even_list will be populated with all even elements in input_list.
    while index < len(input_list):  # while loop iterates by each index in input_list.
        if input_list[index] % 2 == 0:  # a number is even if it is divisible by 2.
            # so an even number can be defined if it has no remainder when halved.
            even_list.append(input_list[index])
            # if number is even, then block causes element to be appended to even_list.
        index += 1
    return even_list
    # Didn't mutate input_list. Added even elements to separate list that is returned.


def sub(reference_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Generate a list which has the element at the start index and the end index-1."""
    range_list: list[int] = (
        []
    )  # again defined an empty list in globals to prevent mutating reference_list.
    if len(reference_list) == 0 or start_index >= len(reference_list) or end_index <= 0:
        return []
        # edge cases return empty list under these conditions.
    if (
        start_index < 0
    ):  # if start_index is negative, then function makes start_index  = 0.
        # in other words, we start at the beginning of the list.
        start_index = 0
    if end_index > len(reference_list):
        end_index = len(reference_list)
        # if end_index is>length of reference_list, end_index is redefined to list's end
    while (
        start_index < end_index
    ):  # we start at start_index so we can disregard all upstream elements.
        range_list.append(reference_list[start_index])
        # so long as we are between start and end_index, we append those list values.
        # list values are appended to empty range_list defined in globals.
        # while loop captures all values corresponding to start_index and end_index-1
        start_index += 1
    return range_list  # return the list with appended values.
    # Did not mutate reference_list.


def add_at_index(mutated_list: list[int], input_element: int, input_index: int) -> None:
    """Modifies input list to place the inputted element in the inputted index."""
    if input_index < 0 or input_index > len(mutated_list):
        raise IndexError("Index is out of bounds for the input list")
    # Defined edge case to raise index error if index is negative or beyond list length.
    mutated_list.append(
        input_element
    )  # add an element to create a space for the input_element to be inserted.
    for index in range(len(mutated_list) - 1, input_index):
        mutated_list[index] = mutated_list[index + 1]
        # set up this for loop that iterates by index.
        # Desigend a for loop that begins at the list's end -> (len(mutated_list)-1)
        # For loop shifts each element after input_index to the right by one spot.
    mutated_list[input_index] = input_element
    # Once we have shifted over the downstream elements, we can insert input_index.

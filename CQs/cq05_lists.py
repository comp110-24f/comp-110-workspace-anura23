"""Mutation functions."""

___author__ = "730478902"


def manual_append(test_list: list[int], element: int) -> None:
    """Will mutate input by appending element to end of list."""
    test_list.append(element)


a: list[int] = [1, 2, 3]
manual_append(a, 2)
print(a)


def double(list_mult: list[int]) -> None:
    """Will mutate input by doubling every element in list_mult."""
    index: int = 0
    while index < len(list_mult):
        list_mult[index] = list_mult[index] * 2
        index += 1


double(a)
print(a)

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)

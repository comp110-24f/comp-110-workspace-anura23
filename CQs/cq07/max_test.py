"""Practice writing a function that modifies a list and writing unit tests!"""

__author__ = "730478902"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_use_case() -> None:
    """Testing find_and_remove_max function returns the largest element in input."""
    assert find_and_remove_max([4, 5, 6, 7]) == 7
    # testing for an expected output.


def test_find_and_remove_max_edge_case() -> None:
    """Testing find_and_remove_max on empty list to ensure -1 is returned."""
    assert find_and_remove_max([]) == -1
    # testing for an unexpected input.


def test_find_and_remove_max_use_case_2() -> None:
    """Testing find_and_remove_max function removes largest element from input."""
    a: list[int] = [9, 8, 7, 6, 9]
    find_and_remove_max(a)
    assert a == [8, 7, 6]
    # testing for desired behavior

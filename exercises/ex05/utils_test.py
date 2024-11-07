"""Implementing Unit Tests for List Utility Functions"""

__author__ = "730478902"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_return_list_use_case() -> None:
    """Testing to see if only_evens returns list with even elements."""
    assert only_evens([11, 12, 13, 14, 15]) == [12, 14]
    # use case associated with proper return behavior.


def test_only_evens_no_mutate_use_case_2() -> None:
    """Testing to see that only_evens does not mutate the inputted list."""
    input_list_test: list[int] = [3, 4, 5, 6, 7]
    only_evens(input_list_test)
    assert input_list_test == [3, 4, 5, 6, 7]
    # use case associated with confirming no mutatating behavior.


def test_only_evens_negative_number_edge_case() -> None:
    """Tests to see whether even numbers that are negative are included in output."""
    edge_case_list: list[int] = [-4, -2, 1, 2, 3]
    assert only_evens(edge_case_list) == [-4, -2, 2]
    # edge case that checks whether negative and positive values are treated similarly


def test_sub_return_list_use_case() -> None:
    """Tests whether sub returns list elements between start index and stop_index-1"""
    sub_test_list: list[int] = [5, 6, 7, 8, 9]
    assert sub(sub_test_list, 1, 4) == [6, 7, 8]
    # use case associated with proper return behavior.


def test_sub_no_mutate_use_case() -> None:
    """Testing to ensure that sub does not mutate the reference_list"""
    reference_list: list[int] = [34, 35, 36, 37]
    sub(reference_list, 0, 2)
    assert reference_list == [34, 35, 36, 37]
    # use case associated with confirming no mutatating behavior.


def test_sub_no_list_length_edge_case() -> None:
    """Testing whether sub returns an empty list if input list is empty."""
    assert sub([], 0, 2) == []
    # edge case to check if empty list is returned when one is inputted.


def test_add_at_index_mutates_use_case() -> None:
    """Testing to see whether add_at_index mutates the input list."""
    mutate_list: list[int] = [9, 11, 12, 13]
    add_at_index(mutate_list, 10, 1)
    assert mutate_list != [9, 10, 12, 13]
    # use case associated with confirming mutatating behavior.


def test_add_at_index_returns_list_use_case() -> None:
    """Testing to see that add_at_index returns list properly mutated with element."""
    test_list: list[int] = [20, 21, 22, 24, 25]
    assert add_at_index(test_list, 23, 3) == [20, 21, 22, 23, 24, 25]
    # use case associated with proper return behavior.


def test_add_at_index_raises_IndexError_edge_case() -> None:
    """Tests that add_at_index raises an IndexError when input index is out of range."""
    with pytest.raises(IndexError):
        add_at_index([90, 91, 92, 93, 95], 94, 7)
    # edge case associated with checking IndexError appearance.

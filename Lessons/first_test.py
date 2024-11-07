from Lessons.unittests import get_first
from Lessons.unittests import remove_and_get_first, remove_first


def test_get_first_use_case() -> None:
    """Testing get_first function returns the first element in a typical input."""
    assert get_first([4, 5, 6, 7]) == 4
    # testing for an expected output.


def test_get_first_edge_case() -> None:
    """Testing get_first on empty list."""
    assert get_first([]) == -1


def test_remove_and_get_first_return_val_use_case() -> None:
    """Testing returning the first element."""
    assert remove_and_get_first([4, 5, 6, 7]) == 4


def test_remove_first_use_case() -> None:
    """Testing remove_first returns nothing."""
    a: list[int] = [4, 5, 6, 7]
    remove_first(a)
    assert a == [5, 6, 7]
    # Testing for desired behavior.


# Did we mutate the list the way we wanted to.


def test_remove_first_edge_case() -> None:
    """Testing remove_first on empty list. Should not do anything/no mutation."""
    a: list[int] = []
    remove_first(a)
    assert a == []


def test_remove_and_first_mutation_use_case() -> None:
    """Testing remove_and_get_first to see if it removes first element in use case."""
    a: list[int] = [4, 5, 6, 7]
    remove_and_get_first(a)
    assert a == [5, 6, 7]

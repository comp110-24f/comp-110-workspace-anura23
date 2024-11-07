def get_first(input: list[int]) -> int:
    """Returns the first element of the input list."""
    if len(input) == 0:
        return -1
    return input[0]


def remove_first(input: list[int]) -> None:
    """Removes the first element of the input list. Does mutate input."""
    if len(input) > 0:
        input.pop(0)


def remove_and_get_first(input: list[int]) -> int:
    """Remove AND return the first element of the input list."""
    first: int = input[0]
    input.pop(0)
    return first  # this way we can actually yield the original first value.


# Motivation for having Unit Tests.
# Instead of testing everything in the REPL by initializing over and over

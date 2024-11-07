"""Practice using while loops for importing practice"""

__author__ = "730478902"


def get_coords(xs: str, ys: str) -> None:
    """Prints the formatted pairs of each character in two input strings."""
    index1: int = 0
    while index1 < len(xs):
        idx2: int = 0
        while idx2 < len(ys):
            print((xs[index1], ys[idx2]))
            idx2 = idx2 + 1
        index1 = index1 + 1
    return None

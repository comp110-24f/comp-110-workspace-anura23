"""Object-Oriented Programming Challenge Question Practice"""

__author__ = "730478902"


class Point:
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init

    # Method Definitions
    def scale_by(self, factor: int) -> None:
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> class:
        

coordinate: Point = Point(x, y)

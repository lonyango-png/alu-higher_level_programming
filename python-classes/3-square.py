#!/usr/bin/python3
"""This module defines a Square class that can compute its own area."""


class Square:
    """A class that defines a square by its size and computes its area."""

    def __init__(self, size=0):
        """Initializes a square with an optional size.

        Args:
            size: the size of the square, must be an integer >= 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2

#!/usr/bin/python3
"""Module that defines a Square class with a size property."""


class Square:
    """Defines a square by its size."""

    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size: the size of the square, must be an integer >= 0.
        """
        self.size = size

    @property
    def size(self):
        """int: the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size, validating type and value.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

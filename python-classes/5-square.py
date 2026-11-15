#!/usr/bin/python3
"""This module defines a Square class that can print itself with #."""


class Square:
    """A class that defines a square by its size and can print it."""

    def __init__(self, size=0):
        """Initializes a square with an optional size.

        Args:
            size: the size of the square, must be an integer >= 0.
        """
        self.size = size

    @property
    def size(self):
        """Gets the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square after validating it.

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
        """Returns the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # to stdout.

        If the size is 0, an empty line is printed instead.
        """
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)

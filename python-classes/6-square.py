#!/usr/bin/python3
"""Module that defines a Square class with a size and a position."""


class Square:
    """Defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square.

        Args:
            size: the size of the square, an integer >= 0.
            position: a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """tuple: the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position, validating it is a tuple of 2 integers.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # at its position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

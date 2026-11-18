#!/usr/bin/python3
"""Module that defines a square based on the rectangle class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square with a private size."""

    def __init__(self, size):
        """Set the size after checking it is a positive integer."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

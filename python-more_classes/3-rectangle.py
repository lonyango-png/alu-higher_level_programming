#!/usr/bin/python3
"""This module defines a Rectangle class that can print itself."""


class Rectangle:
    """A class that defines a rectangle by its width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with an optional width and height.

        Args:
            width: the width of the rectangle, an integer >= 0.
            height: the height of the rectangle, an integer >= 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle after validating it.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle after validating it.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle, or 0 if a side is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the rectangle drawn with the character #.

        An empty string is returned if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        row = "#" * self.__width
        return "\n".join([row] * self.__height)

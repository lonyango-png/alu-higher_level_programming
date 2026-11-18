#!/usr/bin/python3
"""Module that defines a rectangle based on the geometry base class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle with a private width and a private height."""

    def __init__(self, width, height):
        """Set width and height after checking they are positive integers."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

#!/usr/bin/python3
"""Defines the Rectangle class.

The Rectangle class inherits from Base and validates every attribute
before storing it, so the rest of the class can trust its own values.
"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle.

    Private instance attributes, each with a getter and a setter:
        __width, __height, __x and __y.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
            x (int): the x position of the rectangle.
            y (int): the y position of the rectangle.
            id (int): the id of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def __check_integer(name, value):
        """Raise TypeError if value is not an integer.

        Args:
            name (str): the attribute name used in the error message.
            value: the value to check.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width after checking it is an integer greater than 0."""
        self.__check_integer("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height after checking it is an integer greater than 0."""
        self.__check_integer("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get or set the x position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x after checking it is an integer greater or equal to 0."""
        self.__check_integer("x", value)
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get or set the y position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y after checking it is an integer greater or equal to 0."""
        self.__check_integer("y", value)
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area value of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the character #, using x and y offsets."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign attributes from no-keyword or keyword arguments.

        Args:
            *args: the new values in this order: id, width, height, x, y.
            **kwargs: attribute names and values. Skipped if args is
                not empty.
        """
        if args:
            names = ["id", "width", "height", "x", "y"]
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

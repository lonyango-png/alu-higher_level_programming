#!/usr/bin/python3
"""Defines the Square class.

The Square class inherits from Rectangle. A square is a rectangle whose
width and height are always equal, so it reuses all of its validation.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square, a special kind of rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): the size of the square, used for width and height.
            x (int): the x position of the square.
            y (int): the y position of the square.
            id (int): the id of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set width and height, in this order, to the same value."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign attributes from no-keyword or keyword arguments.

        Args:
            *args: the new values in this order: id, size, x, y.
            **kwargs: attribute names and values. Skipped if args is
                not empty.
        """
        if args:
            names = ["id", "size", "x", "y"]
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

#!/usr/bin/python3
"""Module that defines a base class for geometry shapes."""


class BaseGeometry:
    """Base class for geometry shapes."""

    def area(self):
        """Raise an exception because area is not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check that value is an integer greater than 0, else raise."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
"""Module that adds two integers.

This module defines the function add_integer, which adds two numbers
after making sure that both of them are integers or floats. Floats are
cast to integers before the addition is done.
"""


def add_integer(a, b=98):
    """Add two integers and return the result.

    Arguments a and b must be integers or floats. Floats are first cast
    to integers. A TypeError is raised if a or b is not an integer or a
    float. The second argument b defaults to 98.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

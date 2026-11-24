#!/usr/bin/python3
"""Module that prints a square.

This module defines the function print_square, which prints a square
with the character # whose side length is given by the size argument.
The size must be an integer greater than or equal to 0.
"""


def print_square(size):
    """Print a square of the character # with sides of length size.

    The size must be an integer, otherwise a TypeError is raised. If the
    size is less than 0 a ValueError is raised. A size of 0 prints
    nothing at all.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)

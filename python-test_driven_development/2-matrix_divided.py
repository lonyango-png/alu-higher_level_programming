#!/usr/bin/python3
"""Module that divides all the elements of a matrix.

This module defines the function matrix_divided, which divides every
element of a matrix (a list of lists of integers or floats) by a number
and returns a new matrix with the results rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divide all the elements of a matrix by div and return a new matrix.

    The matrix must be a list of lists of integers or floats and every
    row must have the same size, otherwise a TypeError is raised. The
    divisor div must be a number and cannot be 0, otherwise a TypeError
    or a ZeroDivisionError is raised. Results are rounded to 2 decimals.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error)
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]

#!/usr/bin/python3
"""Module that checks if an object is of a class or of a subclass."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass of it."""
    return isinstance(obj, a_class)

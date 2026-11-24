#!/usr/bin/python3
"""Module that prints a name.

This module defines the function say_my_name, which prints a message
made of the text My name is followed by a first name and a last name.
Both names must be strings.
"""


def say_my_name(first_name, last_name=""):
    """Print My name is <first name> <last name>.

    The arguments first_name and last_name must be strings, otherwise a
    TypeError is raised. The last name is optional and defaults to an
    empty string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3
"""Module that prints a text with indentation.

This module defines the function text_indentation, which prints a text
and adds two new lines after each of the characters ., ? and :. No
space is printed at the beginning or at the end of each printed line.
"""


def text_indentation(text):
    """Print text with 2 new lines after each of the characters . ? and :

    The text must be a string, otherwise a TypeError is raised. Spaces at
    the beginning and at the end of every printed line are removed, and
    no new line is added at the end unless the text ends with a delimiter.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    lines = [line.strip(" ") for line in result.split("\n")]
    print("\n".join(lines), end="")

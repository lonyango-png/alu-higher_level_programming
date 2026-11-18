#!/usr/bin/python3
"""Module that defines a list class able to print itself sorted."""


class MyList(list):
    """List subclass with an extra method to print sorted items."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))

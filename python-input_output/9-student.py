#!/usr/bin/python3
"""Module that defines a student with a dictionary description."""


class Student:
    """Student defined by a first name, a last name and an age."""

    def __init__(self, first_name, last_name, age):
        """Set the first name, the last name and the age of the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary description of the student."""
        return self.__dict__

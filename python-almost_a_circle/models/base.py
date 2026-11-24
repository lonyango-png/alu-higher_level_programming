#!/usr/bin/python3
"""Defines the Base class.

The Base class is the foundation of every other class in this project.
It manages the id attribute and the JSON serialization helpers.
"""
import json


class Base:
    """Manage the id attribute and JSON conversion of all other classes.

    Private class attribute:
        __nb_objects (int): number of Base instances created so far.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): the id of the instance. If None, an id is generated
                by incrementing the private class attribute __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): a list of dictionaries.

        Returns:
            "[]" if the list is None or empty, otherwise the JSON string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string of a list of instances to <Class name>.json.

        Args:
            list_objs (list): a list of instances that inherit from Base.
                If None, an empty list is saved. An existing file is
                overwritten.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as jsonfile:
            jsonfile.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string (str): a string representing a list of dictionaries.

        Returns:
            An empty list if json_string is None or empty, otherwise the
            list represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all its attributes already set.

        Args:
            **dictionary (dict): the attributes and their values. A dummy
                instance is created first, then updated with the values.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class name>.json.

        Returns:
            An empty list if the file does not exist, otherwise a list of
            instances of the current class.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                dictionaries = cls.from_json_string(jsonfile.read())
        except FileNotFoundError:
            return []
        return [cls.create(**dictionary) for dictionary in dictionaries]

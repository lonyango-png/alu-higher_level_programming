#!/usr/bin/python3
"""Module that creates an object out of a JSON file."""
import json


def load_from_json_file(filename):
    """Create a Python object out of the JSON text in a file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)

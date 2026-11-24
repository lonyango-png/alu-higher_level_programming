# Python - Almost a circle

A small project that reviews Python classes, inheritance, private
attributes with getters and setters, `*args` and `**kwargs`, JSON
serialization, file reading and writing, and unit testing.

## Classes

- `models/base.py`: `Base`, manages ids and JSON conversion.
- `models/rectangle.py`: `Rectangle`, inherits from `Base`.
- `models/square.py`: `Square`, inherits from `Rectangle`.

## Tests

Run all the unit tests from this folder:

    python3 -m unittest discover tests

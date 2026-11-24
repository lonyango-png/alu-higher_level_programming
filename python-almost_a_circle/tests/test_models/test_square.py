#!/usr/bin/python3
"""Unit tests for the Square class.

Run with: python3 -m unittest tests/test_models/test_square.py
"""
import io
import os
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInit(unittest.TestCase):
    """Test the creation of Square instances."""

    def setUp(self):
        """Reset the id counter before every test."""
        Base._Base__nb_objects = 0

    def test_is_rectangle(self):
        self.assertIsInstance(Square(1), Rectangle)

    def test_is_base(self):
        self.assertIsInstance(Square(1), Base)

    def test_one_arg(self):
        s = Square(5)
        self.assertEqual((s.size, s.x, s.y, s.id), (5, 0, 0, 1))

    def test_two_args(self):
        s = Square(5, 2)
        self.assertEqual((s.size, s.x, s.y), (5, 2, 0))

    def test_three_args(self):
        s = Square(5, 2, 3)
        self.assertEqual((s.size, s.x, s.y), (5, 2, 3))

    def test_four_args(self):
        self.assertEqual(Square(5, 2, 3, 12).id, 12)

    def test_ids_increment(self):
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual((s1.id, s2.id, s3.id), (1, 2, 3))

    def test_width_and_height_equal_size(self):
        s = Square(4)
        self.assertEqual((s.width, s.height), (4, 4))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_no_new_private_size_attribute(self):
        self.assertFalse(hasattr(Square(1), "_Square__size"))

    def test_size_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.5)

    def test_size_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_size_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1])

    def test_size_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_size_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-3)

    def test_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)


class TestSquareSize(unittest.TestCase):
    """Test the size getter and setter."""

    def test_getter(self):
        self.assertEqual(Square(7).size, 7)

    def test_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_setter_updates_width_and_height(self):
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_setter_string(self):
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_setter_float(self):
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = 2.5

    def test_setter_zero(self):
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0

    def test_setter_negative(self):
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -1

    def test_size_follows_width(self):
        s = Square(5)
        s.width = 8
        self.assertEqual(s.size, 8)


class TestSquareStr(unittest.TestCase):
    """Test the __str__ method."""

    def setUp(self):
        """Reset the id counter before every test."""
        Base._Base__nb_objects = 0

    def test_str_defaults(self):
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")

    def test_str_two_args(self):
        self.assertEqual(str(Square(2, 2)), "[Square] (1) 2/0 - 2")

    def test_str_all_args(self):
        self.assertEqual(str(Square(3, 1, 3, 4)), "[Square] (4) 1/3 - 3")

    def test_str_print(self):
        with patch("sys.stdout", new=io.StringIO()) as out:
            print(Square(5, 1, 2, 9))
        self.assertEqual(out.getvalue(), "[Square] (9) 1/2 - 5\n")

    def test_str_after_size_change(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")


class TestSquareInheritedMethods(unittest.TestCase):
    """Test the area and display methods inherited from Rectangle."""

    @staticmethod
    def capture(square):
        """Return what square.display() prints."""
        with patch("sys.stdout", new=io.StringIO()) as out:
            square.display()
        return out.getvalue()

    def test_area(self):
        self.assertEqual(Square(5).area(), 25)

    def test_area_two(self):
        self.assertEqual(Square(2, 2).area(), 4)

    def test_area_three(self):
        self.assertEqual(Square(3, 1, 3).area(), 9)

    def test_display(self):
        self.assertEqual(self.capture(Square(3)), "###\n###\n###\n")

    def test_display_x(self):
        self.assertEqual(self.capture(Square(2, 2)), "  ##\n  ##\n")

    def test_display_x_and_y(self):
        self.assertEqual(self.capture(Square(3, 1, 3)),
                         "\n\n\n ###\n ###\n ###\n")


class TestSquareUpdateArgs(unittest.TestCase):
    """Test the update method with no-keyword arguments."""

    def setUp(self):
        """Create the square used by every test."""
        Base._Base__nb_objects = 0
        self.s = Square(5)

    def test_no_args(self):
        self.s.update()
        self.assertEqual(str(self.s), "[Square] (1) 0/0 - 5")

    def test_one_arg(self):
        self.s.update(10)
        self.assertEqual(str(self.s), "[Square] (10) 0/0 - 5")

    def test_two_args(self):
        self.s.update(1, 2)
        self.assertEqual(str(self.s), "[Square] (1) 0/0 - 2")

    def test_three_args(self):
        self.s.update(1, 2, 3)
        self.assertEqual(str(self.s), "[Square] (1) 3/0 - 2")

    def test_four_args(self):
        self.s.update(1, 2, 3, 4)
        self.assertEqual(str(self.s), "[Square] (1) 3/4 - 2")

    def test_extra_args_ignored(self):
        self.s.update(1, 2, 3, 4, 5, 6)
        self.assertEqual(str(self.s), "[Square] (1) 3/4 - 2")

    def test_args_skip_kwargs(self):
        self.s.update(1, size=9)
        self.assertEqual(self.s.size, 5)

    def test_size_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s.update(1, "2")

    def test_size_value_error(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s.update(1, 0)

    def test_x_error(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.s.update(1, 2, -3)

    def test_y_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.s.update(1, 2, 3, "4")


class TestSquareUpdateKwargs(unittest.TestCase):
    """Test the update method with keyword arguments."""

    def setUp(self):
        """Create the square used by every test."""
        Base._Base__nb_objects = 0
        self.s = Square(5)

    def test_x(self):
        self.s.update(x=12)
        self.assertEqual(str(self.s), "[Square] (1) 12/0 - 5")

    def test_size_and_y(self):
        self.s.update(size=7, y=1)
        self.assertEqual(str(self.s), "[Square] (1) 0/1 - 7")

    def test_size_id_y(self):
        self.s.update(size=7, id=89, y=1)
        self.assertEqual(str(self.s), "[Square] (89) 0/1 - 7")

    def test_kwargs_error(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s.update(size=-1)

    def test_kwargs_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.s.update(x="1")


class TestSquareToDictionary(unittest.TestCase):
    """Test the to_dictionary method."""

    def setUp(self):
        """Reset the id counter before every test."""
        Base._Base__nb_objects = 0

    def test_keys(self):
        d = Square(10, 2, 1).to_dictionary()
        self.assertEqual(sorted(d), ["id", "size", "x", "y"])

    def test_values(self):
        d = Square(10, 2, 1).to_dictionary()
        self.assertEqual(d, {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_type(self):
        self.assertEqual(type(Square(1).to_dictionary()), dict)

    def test_update_with_dictionary(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 == s2)

    def test_dictionary_is_a_copy(self):
        s = Square(3)
        d = s.to_dictionary()
        d["size"] = 99
        self.assertEqual(s.size, 3)

    def test_with_arg(self):
        with self.assertRaises(TypeError):
            Square(1).to_dictionary(1)


class TestSquareSaveToFile(unittest.TestCase):
    """Test the save_to_file class method called on Square."""

    def tearDown(self):
        """Remove the json file created by the tests."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one_square(self):
        Square.save_to_file([Square(1, 0, 0, 5)])
        with open("Square.json") as f:
            self.assertEqual(f.read(),
                             '[{"id": 5, "size": 1, "x": 0, "y": 0}]')


if __name__ == "__main__":
    unittest.main()

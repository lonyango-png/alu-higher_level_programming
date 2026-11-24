#!/usr/bin/python3
"""Unit tests for the Rectangle class.

Run with: python3 -m unittest tests/test_models/test_rectangle.py
"""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """Test the creation of Rectangle instances."""

    def setUp(self):
        """Reset the id counter before every test."""
        Base._Base__nb_objects = 0

    def test_is_base(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_two_args(self):
        r = Rectangle(10, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 0, 0))

    def test_three_args(self):
        r = Rectangle(10, 2, 3)
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 3, 0))

    def test_four_args(self):
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 3, 4))

    def test_five_args(self):
        r = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(r.id, 12)

    def test_ids_increment(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual((r1.id, r2.id, r3.id), (1, 2, 12))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2).__width)

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2).__height)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2).__x)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2).__y)

    def test_mangled_attributes(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r._Rectangle__width, 1)
        self.assertEqual(r._Rectangle__height, 2)
        self.assertEqual(r._Rectangle__x, 3)
        self.assertEqual(r._Rectangle__y, 4)


class TestRectangleWidth(unittest.TestCase):
    """Test the validation of width."""

    def test_width_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.5, 2)

    def test_width_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_width_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1], 2)

    def test_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1}, 2)

    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 2)

    def test_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1}, 2)

    def test_width_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("inf"), 2)

    def test_width_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("nan"), 2)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_width_setter(self):
        r = Rectangle(1, 2)
        r.width = 9
        self.assertEqual(r.width, 9)

    def test_width_setter_negative(self):
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10

    def test_width_setter_string(self):
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = "9"

    def test_width_unchanged_after_error(self):
        r = Rectangle(10, 2)
        try:
            r.width = -1
        except ValueError:
            pass
        self.assertEqual(r.width, 10)


class TestRectangleHeight(unittest.TestCase):
    """Test the validation of height."""

    def test_height_string(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 2.5)

    def test_height_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)

    def test_height_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, False)

    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, [2])

    def test_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {})

    def test_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, (2,))

    def test_height_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float("inf"))

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_height_setter(self):
        r = Rectangle(1, 2)
        r.height = 9
        self.assertEqual(r.height, 9)

    def test_height_setter_zero(self):
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = 0

    def test_height_setter_string(self):
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.height = "9"

    def test_width_checked_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("a", "b")

    def test_width_value_checked_before_height_type(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, "b")


class TestRectangleXY(unittest.TestCase):
    """Test the validation of x and y."""

    def test_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3")

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, 3.5)

    def test_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, None)

    def test_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, True)

    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, [1])

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)

    def test_x_zero(self):
        self.assertEqual(Rectangle(10, 2, 0).x, 0)

    def test_x_setter(self):
        r = Rectangle(1, 2)
        r.x = 9
        self.assertEqual(r.x, 9)

    def test_x_setter_dict(self):
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = {}

    def test_x_setter_negative(self):
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.x = -5

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "4")

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, 4.5)

    def test_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, None)

    def test_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, False)

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, (1,))

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_y_zero(self):
        self.assertEqual(Rectangle(10, 2, 3, 0).y, 0)

    def test_y_setter(self):
        r = Rectangle(1, 2)
        r.y = 9
        self.assertEqual(r.y, 9)

    def test_y_setter_string(self):
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.y = "9"

    def test_y_setter_negative(self):
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.y = -1

    def test_x_checked_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "a", "b")


class TestRectangleArea(unittest.TestCase):
    """Test the area method."""

    def test_area_small(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_area_other(self):
        self.assertEqual(Rectangle(2, 10).area(), 20)

    def test_area_with_position(self):
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_one(self):
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_area_large(self):
        big = 999999999999999
        self.assertEqual(Rectangle(big, big).area(), big * big)

    def test_area_after_change(self):
        r = Rectangle(2, 3)
        r.width = 10
        r.height = 10
        self.assertEqual(r.area(), 100)

    def test_area_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2).area(1)


class TestRectangleDisplay(unittest.TestCase):
    """Test the display method."""

    @staticmethod
    def capture(rect):
        """Return what rect.display() prints."""
        with patch("sys.stdout", new=io.StringIO()) as out:
            rect.display()
        return out.getvalue()

    def test_display_no_offset(self):
        self.assertEqual(self.capture(Rectangle(4, 2)), "####\n####\n")

    def test_display_one_by_one(self):
        self.assertEqual(self.capture(Rectangle(1, 1)), "#\n")

    def test_display_tall(self):
        self.assertEqual(self.capture(Rectangle(2, 3)), "##\n##\n##\n")

    def test_display_x(self):
        self.assertEqual(self.capture(Rectangle(2, 2, 3)), "   ##\n   ##\n")

    def test_display_y(self):
        self.assertEqual(self.capture(Rectangle(2, 2, 0, 2)),
                         "\n\n##\n##\n")

    def test_display_x_and_y(self):
        self.assertEqual(self.capture(Rectangle(2, 3, 2, 2)),
                         "\n\n  ##\n  ##\n  ##\n")

    def test_display_other(self):
        self.assertEqual(self.capture(Rectangle(3, 2, 1, 0)), " ###\n ###\n")

    def test_display_returns_none(self):
        with patch("sys.stdout", new=io.StringIO()):
            self.assertIsNone(Rectangle(1, 1).display())

    def test_display_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1).display(1)


class TestRectangleStr(unittest.TestCase):
    """Test the __str__ method."""

    def setUp(self):
        """Reset the id counter before every test."""
        Base._Base__nb_objects = 0

    def test_str_all_args(self):
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")

    def test_str_defaults(self):
        self.assertEqual(str(Rectangle(5, 5, 1)), "[Rectangle] (1) 1/0 - 5/5")

    def test_str_print(self):
        with patch("sys.stdout", new=io.StringIO()) as out:
            print(Rectangle(2, 3, 4, 5, 6))
        self.assertEqual(out.getvalue(), "[Rectangle] (6) 4/5 - 2/3\n")

    def test_str_after_change(self):
        r = Rectangle(1, 1, 0, 0, 7)
        r.width = 5
        self.assertEqual(str(r), "[Rectangle] (7) 0/0 - 5/1")

    def test_str_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1).__str__(1)


class TestRectangleUpdateArgs(unittest.TestCase):
    """Test the update method with no-keyword arguments."""

    def setUp(self):
        """Create the rectangle used by every test."""
        Base._Base__nb_objects = 0
        self.r = Rectangle(10, 10, 10, 10)

    def test_no_args(self):
        self.r.update()
        self.assertEqual(str(self.r), "[Rectangle] (1) 10/10 - 10/10")

    def test_one_arg(self):
        self.r.update(89)
        self.assertEqual(str(self.r), "[Rectangle] (89) 10/10 - 10/10")

    def test_two_args(self):
        self.r.update(89, 2)
        self.assertEqual(str(self.r), "[Rectangle] (89) 10/10 - 2/10")

    def test_three_args(self):
        self.r.update(89, 2, 3)
        self.assertEqual(str(self.r), "[Rectangle] (89) 10/10 - 2/3")

    def test_four_args(self):
        self.r.update(89, 2, 3, 4)
        self.assertEqual(str(self.r), "[Rectangle] (89) 4/10 - 2/3")

    def test_five_args(self):
        self.r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.r), "[Rectangle] (89) 4/5 - 2/3")

    def test_extra_args_ignored(self):
        self.r.update(89, 2, 3, 4, 5, 6, 7)
        self.assertEqual(str(self.r), "[Rectangle] (89) 4/5 - 2/3")

    def test_args_skip_kwargs(self):
        self.r.update(89, width=1)
        self.assertEqual(self.r.width, 10)

    def test_id_none(self):
        self.r.update(None)
        self.assertIsNone(self.r.id)

    def test_width_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.update(89, "2")

    def test_height_value_error(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r.update(89, 2, 0)

    def test_x_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r.update(89, 2, 3, "4")

    def test_y_value_error(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r.update(89, 2, 3, 4, -5)


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Test the update method with keyword arguments."""

    def setUp(self):
        """Create the rectangle used by every test."""
        Base._Base__nb_objects = 0
        self.r = Rectangle(10, 10, 10, 10)

    def test_height(self):
        self.r.update(height=1)
        self.assertEqual(str(self.r), "[Rectangle] (1) 10/10 - 10/1")

    def test_width_and_x(self):
        self.r.update(width=1, x=2)
        self.assertEqual(str(self.r), "[Rectangle] (1) 2/10 - 1/10")

    def test_all_unordered(self):
        self.r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(self.r), "[Rectangle] (89) 3/1 - 2/10")

    def test_other_order(self):
        self.r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(self.r), "[Rectangle] (1) 1/3 - 4/2")

    def test_kwargs_errors(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.update(width=0)

    def test_kwargs_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.update(y="1")


class TestRectangleToDictionary(unittest.TestCase):
    """Test the to_dictionary method."""

    def setUp(self):
        """Reset the id counter before every test."""
        Base._Base__nb_objects = 0

    def test_keys(self):
        d = Rectangle(10, 2, 1, 9).to_dictionary()
        self.assertEqual(sorted(d), ["height", "id", "width", "x", "y"])

    def test_values(self):
        d = Rectangle(10, 2, 1, 9).to_dictionary()
        self.assertEqual(d, {"id": 1, "width": 10, "height": 2,
                             "x": 1, "y": 9})

    def test_type(self):
        self.assertEqual(type(Rectangle(1, 2).to_dictionary()), dict)

    def test_update_with_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 == r2)

    def test_dictionary_is_a_copy(self):
        r = Rectangle(1, 2)
        d = r.to_dictionary()
        d["width"] = 99
        self.assertEqual(r.width, 1)

    def test_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Unit tests for the Base class.

Run with: python3 -m unittest tests/test_models/test_base.py
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test the id handling and the JSON helpers of the Base class."""

    def setUp(self):
        """Reset the id counter before every test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove the json files created by the tests."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_no_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_ids_increment(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual((b1.id, b2.id, b3.id), (1, 2, 3))

    def test_given_id(self):
        self.assertEqual(Base(12).id, 12)

    def test_given_id_does_not_increment(self):
        Base()
        Base(12)
        self.assertEqual(Base().id, 2)

    def test_id_zero(self):
        self.assertEqual(Base(0).id, 0)

    def test_id_negative(self):
        self.assertEqual(Base(-5).id, -5)

    def test_id_string(self):
        self.assertEqual(Base("abc").id, "abc")

    def test_id_none(self):
        self.assertEqual(Base(None).id, 1)

    def test_id_float(self):
        self.assertEqual(Base(2.5).id, 2.5)

    def test_id_list(self):
        self.assertEqual(Base([1, 2]).id, [1, 2])

    def test_id_is_public(self):
        b = Base(3)
        b.id = 99
        self.assertEqual(b.id, 99)

    def test_nb_objects_is_private(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_nb_objects_value(self):
        Base()
        Base()
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_subclass_shares_counter(self):
        Base()
        r = Rectangle(1, 2)
        s = Square(1)
        self.assertEqual((r.id, s.id), (2, 3))

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_type(self):
        self.assertEqual(type(Base.to_json_string([{"id": 1}])), str)

    def test_to_json_string_one(self):
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')

    def test_to_json_string_two(self):
        data = [{"id": 1}, {"id": 2}]
        self.assertEqual(Base.to_json_string(data), '[{"id": 1}, {"id": 2}]')

    def test_to_json_string_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 1)
        string = Base.to_json_string([r.to_dictionary()])
        self.assertIn('"width": 10', string)
        self.assertIn('"height": 7', string)

    def test_to_json_string_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_two_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_rectangle(self):
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 1)])
        with open("Rectangle.json") as f:
            self.assertEqual(len(f.read()), 53)

    def test_save_to_file_square(self):
        Square.save_to_file([Square(5, 1, 2, 3)])
        with open("Square.json") as f:
            self.assertEqual(Base.from_json_string(f.read()),
                             [{"id": 3, "size": 5, "x": 1, "y": 2}])

    def test_save_to_file_overwrite(self):
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        Rectangle.save_to_file([Rectangle(3, 4, 0, 0, 2)])
        with open("Rectangle.json") as f:
            data = Base.from_json_string(f.read())
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["id"], 2)

    def test_save_to_file_two_objects(self):
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8), Rectangle(2, 4)])
        with open("Rectangle.json") as f:
            self.assertEqual(len(Base.from_json_string(f.read())), 2)

    def test_save_to_file_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_two_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])

    def test_save_to_file_base_has_no_to_dictionary(self):
        with self.assertRaises(AttributeError):
            Base.save_to_file([Base(1)])

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_empty_list(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_type(self):
        self.assertEqual(type(Base.from_json_string('[{"id": 1}]')), list)

    def test_from_json_string_one(self):
        self.assertEqual(Base.from_json_string('[{"id": 89}]'),
                         [{"id": 89}])

    def test_from_json_string_two(self):
        string = '[{"id": 89, "width": 10}, {"id": 7, "width": 1}]'
        self.assertEqual(Base.from_json_string(string),
                         [{"id": 89, "width": 10}, {"id": 7, "width": 1}])

    def test_from_json_string_round_trip(self):
        data = [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]
        string = Base.to_json_string(data)
        self.assertEqual(Base.from_json_string(string), data)

    def test_from_json_string_no_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))

    def test_create_rectangle_is_new_object(self):
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_rectangle_type(self):
        r = Rectangle.create(id=4, width=2, height=3, x=1, y=1)
        self.assertIsInstance(r, Rectangle)

    def test_create_rectangle_partial(self):
        r = Rectangle.create(id=4, width=7)
        self.assertEqual(str(r), "[Rectangle] (4) 0/0 - 7/1")

    def test_create_square(self):
        s1 = Square(3, 5, 1)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))

    def test_create_square_is_new_object(self):
        s1 = Square(3, 5, 1)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsNot(s1, s2)

    def test_create_square_type(self):
        s = Square.create(id=4, size=2, x=1, y=1)
        self.assertIsInstance(s, Square)

    def test_create_base(self):
        class Dummy(Base):
            def update(self, *args, **kwargs):
                for key, value in kwargs.items():
                    setattr(self, key, value)

        obj = Dummy.create(id=77)
        self.assertEqual(obj.id, 77)

    def test_load_from_file_missing(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_missing_square(self):
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_empty_list(self):
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(r1))
        self.assertEqual(str(loaded[1]), str(r2))

    def test_load_from_file_rectangle_type(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertIsInstance(Rectangle.load_from_file()[0], Rectangle)

    def test_load_from_file_squares(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(s1))
        self.assertEqual(str(loaded[1]), str(s2))

    def test_load_from_file_square_type(self):
        Square.save_to_file([Square(1)])
        self.assertIsInstance(Square.load_from_file()[0], Square)

    def test_load_from_file_new_objects(self):
        r1 = Rectangle(1, 2)
        Rectangle.save_to_file([r1])
        self.assertIsNot(Rectangle.load_from_file()[0], r1)

    def test_load_from_file_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file(1)


if __name__ == "__main__":
    unittest.main()

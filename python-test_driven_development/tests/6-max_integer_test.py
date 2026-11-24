#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for the function max_integer."""

    def test_ordered_list(self):
        """Test a list sorted in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list that is not sorted."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list with the max value at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test a list with the max value in the middle."""
        self.assertEqual(max_integer([1, 2, 9, 3, 4]), 9)

    def test_max_at_end(self):
        """Test a list with the max value at the end."""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Test the default argument."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test a list with only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_zeros(self):
        """Test lists made of zeros."""
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        self.assertEqual(max_integer([-5, -2, -10]), -2)
        self.assertEqual(max_integer([-3, -1, -2]), -1)

    def test_mixed_signs(self):
        """Test a list of negative, zero and positive numbers."""
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([1, 0, -1]), 1)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_ints_and_floats(self):
        """Test a list that mixes integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_duplicate_max(self):
        """Test a list where the max value appears twice."""
        self.assertEqual(max_integer([4, 4, 1]), 4)

    def test_all_equal(self):
        """Test a list where all the values are equal."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_big_numbers(self):
        """Test a list with very big numbers."""
        self.assertEqual(max_integer([10 ** 20, 1]), 10 ** 20)

    def test_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_tuple(self):
        """Test a tuple instead of a list."""
        self.assertEqual(max_integer((1, 5, 3)), 5)

    def test_list_not_modified(self):
        """Test that the list is not modified by the function."""
        numbers = [1, 3, 2]
        max_integer(numbers)
        self.assertEqual(numbers, [1, 3, 2])

    def test_none_argument(self):
        """Test None instead of a list."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_integer_argument(self):
        """Test an integer instead of a list."""
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_mixed_types(self):
        """Test a list that mixes integers and strings."""
        with self.assertRaises(TypeError):
            max_integer([1, "a"])

    def test_none_in_list(self):
        """Test a list that contains None."""
        with self.assertRaises(TypeError):
            max_integer([None, 1])
        with self.assertRaises(TypeError):
            max_integer([1, None])


if __name__ == '__main__':
    unittest.main()

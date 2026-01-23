#!/usr/bin/python3
import unittest
add_integer = __import__('0-add_integer').add_integer


class TestAddInteger(unittest.TestCase):
    """Tests for add_integer function"""

    def test_add_integers(self):
        self.assertEqual(add_integer(1, 2), 3)
        self.assertEqual(add_integer(100, 0), 100)
        self.assertEqual(add_integer(-5, -3), -8)

    def test_add_floats(self):
        self.assertEqual(add_integer(1.5, 2.3), 3)
        self.assertEqual(add_integer(3.9, 2), 5)

    def test_mixed_types(self):
        self.assertEqual(add_integer(5, 2.7), 7)
        self.assertEqual(add_integer(2.7, 5), 7)

    def test_default_b(self):
        self.assertEqual(add_integer(2), 100)

    def test_type_error_a(self):
        with self.assertRaises(TypeError):
            add_integer("1", 2)

    def test_type_error_b(self):
        with self.assertRaises(TypeError):
            add_integer(1, "2")

    def test_none(self):
        with self.assertRaises(TypeError):
            add_integer(None)

    def test_bool(self):
        self.assertEqual(add_integer(True, True), 2)


if __name__ == "__main__":
    unittest.main()

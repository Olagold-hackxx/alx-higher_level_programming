#!/usr/bin/python3
""" Unittest for func max_integer """


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(max_integer.__doc__)

    def test_empty(self):
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 9]), 9)
        self.assertEqual(max_integer([5, -2, 12]), 12)
        self.assertEqual(max_integer([5.5, 8.6, 65.20]), 65.20)
        self.assertEqual(max_integer([-5.5, -8.6, -65.20]), -5.5)
        self.assertEqual(max_integer(["a", "z"]), "z")
        self.assertEqual(max_integer(["apple", "zombie"]), "zombie")

    def test_errors(self):
        self.assertRaises(TypeError, max_integer, [1, "a"])


if __name__ == "__main__":
    unittest.main()

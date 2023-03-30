#!/usr/bin/env python3

"""Define unittests for base.py"""


from json.tool import main
import unittest
from models.base import Base
from models.rectangle import Rectangle

class Test_Base(unittest.TestCase):
    def setUp(self):
        """Hold constant value for all test cases"""
        Base._Base__nb_objects = 0
    
    def tearDown(self):
        """Wipe constant value"""

    def test_initialize_id(self):
        """Initialize and increment id if None or no arg passsed"""
        b = Base()
        self.assertEqual(b.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(None)
        self.assertEqual(b3.id, 3)

    def test_assign_id(self):
        b = Base(8)
        self.assertEqual(b.id, 8)
    
    def test_alltypes(self):
        """Test id accept all types and raise no Exception"""
        b = Base('id')
        self.assertTrue(b.id == 'id')

        b2 = Base([2, 3])
        self.assertTrue(b2.id == [2, 3])

        b3 = Base(('tuple', 1))
        self.assertTrue(b3.id == ('tuple', 1))

        b4 = Base({1, 2})
        self.assertTrue(b4.id == {1, 2})

    def test_float_overflow(self):
        """Float overflow"""
        b = Base(float('inf'))
        self.assertEqual(b.id, float('inf'))

    def test_private_attr(self):
        """Private instance counter is present"""
        self.assertTrue('_Base__nb_objects' in Base.__dict__)


if __name__ == "__main__":
    unittest.main()
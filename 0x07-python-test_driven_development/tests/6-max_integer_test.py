#!/usr/bin/python3
'''Module to implement unittests
'''

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''A Test case
    '''

    def test_values(self):
        self.assertIsNone(max_integer())
        self.assertEqual(max_integer([10, 50, 30, 40]), 50)
        self.assertEqual(max_integer([10, -50, 30, 40]), 40)
        self.assertEqual(max_integer([-10, -50, -30, -40]), -10)
        self.assertEqual(max_integer("snake"), "s")
        self.assertEqual(max_integer([150]), 150)
        self.assertRaises(TypeError, max_integer, 10)


if __name__ == '__main__':
    unittest.main()

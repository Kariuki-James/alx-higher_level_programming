#!/usr/bin/python3
'''Tests for 'models/rectangle' module'''

import unittest
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    '''TestCase for the Rectangle class'''

    def test_rectangle_initialization(self):
        '''Tests instatiation of Rectangle objects'''
        r1 = Rectangle(10, 2)

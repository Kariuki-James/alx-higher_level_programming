#!/usr/bin/python3
'''Tests for 'models/base' module'''

import unittest
from models.base import Base



class TestBase(unittest.TestCase):
    '''TestCase for the Base class'''

    def test_base_id_allocation(self):
        '''Tests if Base objects are assigned ids correctly'''
        b1 = Base()
        b2 = Base()
        b3 = Base(15)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 15)

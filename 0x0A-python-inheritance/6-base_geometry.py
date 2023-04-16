#!/usr/bin/python3
'''This module defines a Geometrical class.'''


class BaseGeometry:
    '''defines a geometrical object'''
    
    def area(self):
        '''empty method, raises an exception'''
        raise Exception("area() is not implemented")

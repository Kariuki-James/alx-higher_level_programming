#!/usr/bin/python3
'''This is a Geometry module'''


class BaseGeometry:
    '''Instantiates a geometrical object'''

    def area(self):
        '''empty method, raises an exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

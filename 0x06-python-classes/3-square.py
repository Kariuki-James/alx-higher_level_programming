#!/usr/bin/python3

"""This module defines a square"""


class Square:
    """Represents a mathematical square

    Args:
        size (int): The size of the square
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''compute area of square'''

        return self.__size ** 2

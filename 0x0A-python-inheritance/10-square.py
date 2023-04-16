#!/usr/bin/python3
'''This modules defines a square'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Represents a square (width == height)'''

    def __init__(self, size):
        super().__init__(size, size)

#!/usr/bin/python3
'''Square module'''
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Represents a square

    Args:
        size (int): width/height of the square
        x (int): x-coordinate of the square
        y (int): y-coordinate of the square
        id (int): unique identifier of the object
    '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} "\
                f"- {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

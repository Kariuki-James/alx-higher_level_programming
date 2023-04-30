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

    def update(self, *args, **kwargs):
        '''assigns attributes

        Args:
            *args: tuple containing attributes.
                arg[0] (int): id
                arg[1] (int): size
                arg[2] (int): x
                arg[3] (int): y
            **kwargs: key-worded values for each attribute.
                Only used if `*args` is not present or is empty.
        '''
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            elif i == 1:
                self.size = arg
            elif i == 2:
                self.x = arg
            elif i == 3:
                self.y = arg

        if not args:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

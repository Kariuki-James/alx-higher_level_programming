#!/usr/bin/python3
'''Rectangle module'''
from models.base import Base


class Rectangle(Base):
    '''Represents a rectangle

    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): x-coordinate of the rectangle
        y (int): y-coordinate of the rectangle
        id (int): unique identifier of the object
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.set_width(width)
        self.set_height(height)
        self.set_x(x)
        self.set_y(y)

        Base.__init__(self, id)

    def set_width(self, width):
        '''width setter'''
        self.__width = width

    def get_width(self):
        '''width getter'''
        return self.__width

    def set_height(self, height):
        '''height setter'''
        self.__height = height

    def get_height(self):
        '''height getter'''
        return self.__height

    def set_x(self, x):
        '''x setter'''
        self.__x = x

    def get_x(self):
        '''x getter'''
        return self.__x

    def set_y(self, y):
        '''y setter'''
        self.__y = y

    def get_y(self):
        '''y getter'''
        return self.__y

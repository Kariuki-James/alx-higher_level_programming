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
        self.setWidth(width)
        self.setHeight(height)
        self.setX(x)
        self.setY(y)

        Base.__init__(self, id)

    def setWidth(self, width):
        '''width setter'''
        self.__width = width

    def getWidth(self):
        '''width getter'''
        return self.__width

    def setHeight(self, height):
        '''height setter'''
        self.__height = height

    def getHeight(self):
        '''height getter'''
        return self.__height

    def setX(self, x):
        '''x setter'''
        self.__x = x

    def getX(self):
        '''x getter'''
        return self.__x

    def setY(self, y):
        '''y setter'''
        self.__y = y

    def getY(self):
        '''y getter'''
        return self.__y

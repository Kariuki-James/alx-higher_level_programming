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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        Base.__init__(self, id)

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, width):
        '''width setter'''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, height):
        '''height setter'''
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, x):
        '''x setter'''
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, y):
        '''y setter'''
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} "\
                f"- {self.width}/{self.height}"

    def area(self):
        '''computes area of a rectangle'''
        return self.width * self.height

    def display(self):
        '''prints the rectangle instance with the character `#`'''
        for y_coord in range(self.y):
            print()

        for row in range(self.height):
            for x_coord in range(self.x):
                print(end=' ')

            for col in range(self.width):
                print('#', end='')
            print()

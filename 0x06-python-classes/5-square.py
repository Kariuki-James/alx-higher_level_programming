#!/usr/bin/python3

"""This module defines a square"""


class Square:
    """Represents a mathematical square

    Args:
        size (int): The size of the square
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        Calculates the area of a square
        '''
        return (self.__size ** 2)

    def my_print(self):
        '''
        prints in stdout the square with character '#'
        '''

        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print('#', end='')
                print()

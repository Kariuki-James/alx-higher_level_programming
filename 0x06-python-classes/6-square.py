#!/usr/bin/python3

"""This module defines a square"""


class Square:
    """Represents a mathematical square

    Args:
        size (int): The size of the square
        position (int, int):
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
                for pos in range(self.position[0]):
                    print(' ', end='')
                for j in range(self.size):
                    print('#', end='')
                print()

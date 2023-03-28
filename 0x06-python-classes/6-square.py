#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """Represents a mathematical square

    Args:
        size (int): The size of the square
        position (int, int): Coordinates of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        '''get size of a square'''

        return (self.__size)

    @size.setter
    def size(self, size):
        '''set size of a square'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        '''get the position of a square'''

        return (self.__position)

    @position.setter
    def position(self, position):
        '''set the position of a square'''

        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in position):
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
            for vertical in range(self.position[1]):
                print()

            for row in range(self.size):
                for pos in range(self.position[0]):
                    print(' ', end='')
                for col in range(self.size):
                    print('#', end='')
                print()

#!/usr/bin/python3
""" This module creates a Rectangle class.
"""


class Rectangle():
    """Represents a Rectangle

    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle

    Attributes:
        number_of_instances (int): The number of active Rectangle instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        rect = []
        if self.__width == 0 or self.__height == 0:
            return ("")
        for row in range(self.__height):
            for col in range(self.__width):
                rect.append("#")

            # add newline to all lines except the last one
            if row < (self.__height - 1):
                rect.append('\n')
        return ("".join(rect))

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """width of rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height of rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle

        Returns:
            int: The area of the rectangle
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of a rectangle

        Returns:
            int: The perimeter of the rectangle
        """

        perimeter = 0
        if self.__width != 0 and self.__height != 0:
            perimeter = (self.__width + self.__height) * 2

        return perimeter

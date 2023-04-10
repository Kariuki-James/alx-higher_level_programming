#!/usr/bin/python3
"""Defines a function that adds 2 integers"""

def add_integer(a, b=98):
    '''
    Adds 2 integers

    Args:
        a (int/float): first integer
        b (int/float): second integer
    Returns:
        int/float: The addition of 'a' and 'b'
    '''

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

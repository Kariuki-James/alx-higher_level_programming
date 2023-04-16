#!/usr/bin/python3
''' This module defines a function that checks object instances'''


def is_same_class(obj, a_class):
    '''checks if an object is exactly an instance of a specified class.

    Args:
        obj (object): any object
        a_class (class): any class
    Returns:
        True, if @obj is exactly an instance of @a_class
        Otherwise, False
    '''
    if type(obj) == a_class:
        return True
    return False

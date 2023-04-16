#!/usr/bin/python3
'''This module checks for Inheritance in Objects'''


def is_kind_of_class(obj, a_class):
    '''checks if an object is an instance of, or if the object is an
    instance of a class that inherited from the specified class.

    Args:
        obj (object): any object
        a_class (class): any class
    Returns:
        True if @obj is an instance of @a_class
    '''
    return isinstance(obj, a_class)

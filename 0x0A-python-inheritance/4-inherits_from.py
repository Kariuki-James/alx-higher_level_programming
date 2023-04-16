#!/usr/bin/python3
'''This module checks for subclasses'''


def inherits_from(obj, a_class):
    '''checks if an object is a subclass of a specified class

    Returns:
        True if @obj is a subclass of @a_class.
        Otherwise, False
    '''
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False

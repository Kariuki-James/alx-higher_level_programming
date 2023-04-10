#!/usr/bin/python3
'''Defines a function that prints names'''


def say_my_name(first_name, last_name=""):
    '''
    Prints a person's first name and last name

    Args:
        first_name (string): the first name
        last_name (string): the last name
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

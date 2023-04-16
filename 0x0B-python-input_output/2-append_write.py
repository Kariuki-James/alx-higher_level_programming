#!/usr/bin/python3
'''This module defines a function that appends text to file'''


def append_write(filename="", text=""):
    '''appends a string at the end of a text file (utf-8)

    Returns:
        The number of characters added
    '''
    with open(filename, "a", encoding="utf-8") as file_handler:
        return file_handler.write(text)

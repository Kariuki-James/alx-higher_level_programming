#!/usr/bin/python3
'''This module defines a function to write files'''


def write_file(filename="", text=""):
    '''writes a string to a text file (utf-8)

    Returns:
        The number of characters written
    '''
    with open(filename, "w", encoding="utf-8") as file_handler:
        return file_handler.write(text)

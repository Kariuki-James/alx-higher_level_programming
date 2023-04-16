#!/usr/bin/python3
'''This module defines a function to read text files'''


def read_file(filename=""):
    '''reads a text file (UTF8) and prints it to stdout'''
    with open(filename, encoding="utf-8") as file_handler:
        for line in file_handler:
            print(line, end="")

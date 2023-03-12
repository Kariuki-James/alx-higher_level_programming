#!/usr/bin/python3

def no_c(my_string):
    if my_string is None:
        return

    char_list = [char for char in my_string if char != 'c' and char != 'C']
    new_string = ''.join(char_list)

    return new_string

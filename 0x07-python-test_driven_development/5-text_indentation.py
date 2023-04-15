#!/usr/bin/python3
'''Defines a function that prints text with new lines'''


def text_indentation(text):
    '''
    Prints a text with 2 new lines after each of these characters.
    '.', '?', and ':'

    Args:
        text (str): the text to be printed.
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimeters = ['.', '?', ':']
    words = text.split()
    counter = 0
    for word in words:
        if counter > 0:
            print(' ', end='')

        for char in word:
            if char in delimeters:
                print("{}\n".format(char))
                counter = 0
            else:
                print(char, end='')
                counter += 1

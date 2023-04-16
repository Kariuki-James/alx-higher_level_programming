#!/usr/bin/python3
'''Defines a Class that inherits from 'list'
'''


class MyList(list):
    '''A 'list' subclass'''

    def print_sorted(self):
        '''prints a list of ints in sorted ascending order'''

        print(sorted(self))

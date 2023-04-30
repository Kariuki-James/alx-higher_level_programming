#!/usr/bin/python3
'''This module defines the base class for the entire project'''
import json


class Base:
    '''Base class for other classes'''

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''serializes an Python object to JSON string representation.

        Args:
            list_dictionaries (any): any Python object.

        Returns:
            returns the JSON string representation of @list_dictionaries.
        '''
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

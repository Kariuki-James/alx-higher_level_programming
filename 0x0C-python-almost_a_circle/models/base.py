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
        '''serializes a list of Python dictionaries to JSON string representation.

        Args:
            list_dictionaries (list): a list of dictionaries

        Returns:
            returns the JSON string representation of @list_dictionaries.
        '''
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes JSON representation of @list_objs to a file'''

        filename = f"{cls.__name__}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs:
                list_dictionaries = [x.to_dictionary() for x in list_objs]
                f.write(Base.to_json_string(list_dictionaries))
            else:
                json.dump([], f)

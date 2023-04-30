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
        '''serializes Python dictionaries to JSON string.

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
        '''writes JSON representation of objects to a file

        Args:
            list_objs (list): a list of objects
        '''

        filename = f"{cls.__name__}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs:
                list_dictionaries = [x.to_dictionary() for x in list_objs]
                f.write(Base.to_json_string(list_dictionaries))
            else:
                json.dump([], f)

    @staticmethod
    def from_json_string(json_string):
        '''returns a Python list from JSON string

        Args:
            json_string (str): a string representing a list of dictionaries
        '''
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set

        Args:
            **dictionary (dict)
        '''
        if cls.__name__ == "Rectangle":
            new_obj = cls(width=10, height=10)
            new_obj.update(**dictionary)
        if cls.__name__ == "Square":
            new_obj = cls(size=10)
            new_obj.update(**dictionary)
        return new_obj

#!/usr/bin/python3
'''Student module'''


class Student:
    '''Instantiates a student'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student instance'''

        if type(attrs) == list and \
                all(isinstance(item, str) for item in attrs):
            new_dict = {}
            for attr in attrs:
                try:
                    new_dict.update({attr: getattr(self, attr)})
                except AttributeError:
                    continue
            return new_dict

        return self.__dict__

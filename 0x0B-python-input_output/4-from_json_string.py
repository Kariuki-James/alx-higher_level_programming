#!/usr/bin/python3
'''This module deserializes JSON objects'''

import json


def from_json_string(my_str):
    '''Converts a JSON string representation to a python object

    Returns:
        The python object (python data structure)
    '''

    return json.loads(my_str)

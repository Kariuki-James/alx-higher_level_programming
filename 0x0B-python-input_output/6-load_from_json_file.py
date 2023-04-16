#!/usr/bin/python3
'''This module loads objects from json files'''

import json


def load_from_json_file(filename):
    '''creates an object from a "JSON file"'''

    with open(filename, encoding="utf-8") as file_handler:
        data = json.load(file_handler)
        return data

#!/usr/bin/python3
'''This module saves objects to json file'''

import json


def save_to_json_file(my_obj, filename):
    '''writes an object to a text file, using a JSON representation'''

    with open(filename, "w", encoding="utf-8") as file_handler:
        file_handler.write(json.dumps(my_obj))

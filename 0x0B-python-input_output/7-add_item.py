#!/usr/bin/python3
'''This script adds all arguments to a Python list
and then save them to a file'''

if __name__ != "__main__":
    quit()

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file_name = "add_item.json"
arg_list = []

arg_list.extend(sys.argv[1:])

try:
    json_list = load_from_json_file(file_name)
    json_list.extend(arg_list)
    save_to_json_file(json_list, file_name)
except Exception as e:
    save_to_json_file(arg_list, file_name)

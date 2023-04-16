#!/usr/bin/python3
"""This module finds the dictionary representation of an Object"""


def class_to_json(obj):
    return obj.__dict__

#!/usr/bin/python3
"""A function that returns the dictionary description with simple data struct"""


def class_to_json(obj):
    return obj.__dict__

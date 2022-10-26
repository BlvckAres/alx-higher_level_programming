#!/usr/bin/python3
""" A function that returns the JSON representation of an obj."""
import json


def to_json_string(my_obj):
    """Returns the JSON version of a string."""
    return json.dumps(my_obj)

#!/usr/bin/python3
""" A function that writes an object to a text file, using JSON."""
import json


def save_to_json_file(my_obj, filename):
    """ Returns a JSON representation of a string object."""  
    with open(filename,'w') as f:
        json.dump(my_obj, f)

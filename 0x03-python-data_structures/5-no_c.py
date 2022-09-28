#!/usr/bin/python3
def no_c(my_string):
    char_to_remove = ["C","c"]
    new_string = ""
    for char in my_string:
        if char not in char_to_remove:
            new_string += char
    return new_string

#!/usr/bin/python3
"""Defines a function that prints the first and last name."""


def say_my_name(first, last_name=""):
    """The function prints out the the names with a phrase "My name is".


    Args:
        first_name (str): first name to print
        last_name (str): last name to print

    Raises:
        TypeError: If either of the first_name or last_name are not str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Appends a string.

     Args:
        filename (str): Name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        Characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

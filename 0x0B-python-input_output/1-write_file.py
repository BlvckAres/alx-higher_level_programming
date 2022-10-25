#!/usr/bin/python3
""" A file writing function. """


def write_file(filename="", text=""):
    """Write a string in a file.

     Args:
        filename (str): Name of the file to write.
        text (str): The text to write to the file.
    Returns:
        Characters written in the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

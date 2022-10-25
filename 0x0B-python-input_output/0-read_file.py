#!/usr/bin/python3
""" This function reads a text file(UTF8)."""


def read_file(filename=""):
    """Print the contents of UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

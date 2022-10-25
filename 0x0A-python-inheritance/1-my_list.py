#!/usr/bin/python3
"""Defines an list class MyList."""


class MyList(list):
    """Executes sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints a list in ascending order."""
        print(sorted(self))

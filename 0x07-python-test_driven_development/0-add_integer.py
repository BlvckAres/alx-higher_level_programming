#!/usr/bin/python3
"""Defines a function that adds integars."""


def add_integer(a, b=98):
    """Return the integar addition of a and b.
    Check whether the inputs are the correct type (int),
    then if correct cast ints and return the sum.

    Raises:
      TypeError: If either a or b is non-integar and non-float.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return (int(a) + int(b))

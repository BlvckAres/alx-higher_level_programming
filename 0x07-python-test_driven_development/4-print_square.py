#!/usr/bin/python3
"""Defining a function that prints a square."""


def print_square(size):
    """
    The square is printed with the '#' character.

    Input:
        size (int): The input has to be an int, and is the height/width.

    Raise:
        TypeError: If size is not an int
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("") 

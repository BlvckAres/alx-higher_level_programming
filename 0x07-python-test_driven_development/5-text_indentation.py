#!/usr/bin/python3
"""A function that defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError("text must be a string")
    n = "".join([c if c not in "?.:" else c + "\n\n" for c in text])
    print("\n".join([line.strip() for line in n.split("\n")]), end="")

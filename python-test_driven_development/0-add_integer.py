#!/usr/bin/python3
"""
Module that contains a function to add two integers
"""
def add_integer(a, b=98):
    """
    Adds two integers.

    a and b must be integers or floats.
    Floats are casted to integers.

    Raises:
        TypeError: if a or b is not an integer or float

    Returns:
        int: the addition of a and b
    """
    if not isinstance (a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError ("b must be an integer")

    return int(a) + int(b)

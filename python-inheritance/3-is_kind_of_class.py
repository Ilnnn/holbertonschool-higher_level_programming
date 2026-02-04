#!/usr/bin/python3
"""
This module defines a function that checks if an object
is an instance of a given class or of a class that inherits from it.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or of a class that inherited from it."""
    return isinstance(obj, a_class)

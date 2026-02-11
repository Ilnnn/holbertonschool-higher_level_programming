#!/usr/bin/python3
"""Return an object represented by a JSON string."""


def from_json_string(my_str):
    """Return a Python object represented by a JSON string."""
    return __import__("json").loads(my_str)

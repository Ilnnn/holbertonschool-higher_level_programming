#!/usr/bin/python3
"""Return JSON representation of an object."""


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string."""
    return __import__("json").dumps(my_obj)

#!/usr/bin/python3
"""Write an object to a text file using JSON representation."""


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        __import__("json").dump(my_obj, f)

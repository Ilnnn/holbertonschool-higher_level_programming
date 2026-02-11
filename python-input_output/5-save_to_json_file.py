#!/usr/bin/python3
"""Write an object to a text file using JSON representation."""


def save_to_json_file(my_obj, filename):
    """Serialize an object to a file as JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        __import__("json").dump(my_obj, f)

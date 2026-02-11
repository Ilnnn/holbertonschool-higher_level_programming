#!/usr/bin/python3
"""Write string to UTF8 file."""


def write_file(filename="", text=""):
    """Write text to a file and return number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        returnf.write(text)

#!/usr/bin/python3
"""Append string to UTF8 file."""

def append_write(filename="", text=""):
    """Append a string to the end of a UTF-8 text file and return number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

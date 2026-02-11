#!/usr/bin/python3
"""Append string to UTF8 file."""


def append_write(filename="", text=""):
    """App string to end of UTF-8 text file, return the numb of char added."""
    with open(filename, "a", encoding="utf-8") as f:
        nb_chars = f.write(text)
    return f.write(text)

#!/usr/bin/python3
def append_write(filename="", text=""):
    """App string to end of UTF-8 text file, return the numb of char added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
and provides a method to print the list in sorted order.
"""


class MyList(list):
    """Class that inherits from list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))

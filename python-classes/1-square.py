#!/usr/bin/python3
"""Defines a Square class with a size attribute."""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size):
        """
        Initializes a new Square.

        Args:
            size (int): The size of the square's side.
        """
        self.__size = size

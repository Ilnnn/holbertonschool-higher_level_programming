#!/usr/bin/python3
"""Defines a Square class with size validation."""


class Square:
    """Represents a square with a validated private size."""

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): Length of the square's side.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

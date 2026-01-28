#!/usr/bin/python3
"""Defines a Square class with size property and area calculation."""


class Square:
    """Represents a square with a validated private size."""

    def __init__(self, size=0):
        """Initializes a Square instance."""
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): Length of the square's side.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

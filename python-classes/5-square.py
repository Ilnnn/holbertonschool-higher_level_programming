#!/usr/bin/python3
"""Defines a Square class with size control, area, and print methods."""


class Square:
    """Represents a square with a validated private size."""
    def __init__(self, size=0):
        """Initializes a Square instance."""
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square using '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)

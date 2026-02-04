#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle,
validates size, computes area, and provides a string representation.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize square with validated size.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    
    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
    
    def __str__(self):
        """Return the square description."""
        return f"[Square] {self.__size}/{self.__size}"

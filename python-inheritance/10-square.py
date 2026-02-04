#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle,
validates size, and computes the area of the square.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry 

class Square(Rectangle):
    """Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

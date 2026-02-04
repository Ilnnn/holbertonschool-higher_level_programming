#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry,
validates width and height, computes area, and provides a string representation.
"""


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry."""

    def __init__(self, withd, height):
        """Initialize rectangle with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height
    
    def __str__(self):
        """Return the rectangle description."""
        return f"[Rectangle] {self.__width}/{self.__height}"

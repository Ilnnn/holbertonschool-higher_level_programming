#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry
and validates width and height as positive integers.
"""


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry."""

    def __init__(self, withd, height):
        """Initialize rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

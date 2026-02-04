#!/usr/bin/python3
class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry."""

    def __init__(self, withd, height):
        """Initialize rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

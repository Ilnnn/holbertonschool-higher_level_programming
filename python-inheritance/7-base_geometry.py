#!/usr/bin/python3
"""Module with class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Method for calculated area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for integer validation"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
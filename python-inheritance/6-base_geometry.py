#!/usr/bin/python3
"""
This module defines a base class BaseGeometry
with a method that must be implemented by subclasses.
"""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raises an exception because area is not implemented."""
        raise Exception("area() is not implemented")

#!/usr/bin/python3

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes."""

    def area(self):
        pass
    
    def perimeter(self):
        pass

    import math
    
    class Circle(Shape):
        """Circle shape."""

        def __init___(self, radius):
            self.radius = radius

        def area(self):
            return math.pi * self.radius ** 2

        def perimeter(self):
            return 2 * math.pi * self.radius
        
        class Rectangle(Shape):
            """Rectangle shape."""
        
        def __init__(self, width, height):
            self.width = width
            self.height = height
        
        def area(self):
            return self.width * self.height
        
        def perimeter(self):
            return 2 * (self.width + self.height)

        def shape_info(shape):
            """Print area and perimeter of any shape-like object."""
            print("Area:", shape.area())
            print("Perimeter:", shape.perimeter())

#!/usr/bin/python3
"""Abstract Base Class Animal"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass

    class Dog(Animal):
        """Dog class inheriting from Animal."""
        def sound(self):
            return "Bark"
    
    class Cat(Animal):
        """Cat class inheriting from Animal."""
        def sound(self):
            return "Meow"

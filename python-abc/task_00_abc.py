#!/usr/bin/python3

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals."""

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

#!/usr/bin/python3

class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the Student instance.
        
        If attrs is a list of strings, only include those attributes.
        Otherwise, include all attributes.
        """
            
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
                
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}

        return self.__dict__.copy()

        def reload_from_jason(self, json):
             """Replace all attributes of the Student instance with the ones from json.

        Args:
            json (dict): A dictionary containing attribute names as keys
                         and attribute values as values.
        """
        for key, value in json.items():
            setattr(self, key, value)

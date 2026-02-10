#!/usr/bin/python3
import pickle 

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name" + self.name)
        print("Age" + self.age)
        print("Is Student: " + self.is_student)
    
    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None
    
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)

                if isinstance(obj, cls):
#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): Dictionary to save.
        filename (str): Output JSON file name.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and convert it to Python.

    Args:
        filename (str): JSON file to read.

    Returns:
        dict: Python dictionary obtained after deserialization.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

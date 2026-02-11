#!/usr/bin/python3
"""JSON serialization utility."""


def class_to_json(obj):
    """Return dictio description of an object for JSON serialization."""
    return obj.__dict__

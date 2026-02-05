#!/usr/bin/python3

class CountedIterator:
    """Iterator that counts how many items have been fetched."""

    def __init__(self, iterable):
        self.iterator = inter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        return self
    
    def get_count(self):
        return self.count

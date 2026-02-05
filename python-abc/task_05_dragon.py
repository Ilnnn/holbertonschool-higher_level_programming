#!/usr/bin/python3

class SwimMixin:
    """Mixin for swimming behavior."""
    def swim(self):
        print("The creature swims")


class FlyMixin:
    """Mixin for flying behavior."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon can swim and fly."""
    def roar(self):
        print("The creature roars!")

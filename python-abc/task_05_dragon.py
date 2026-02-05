#!/usr/bin/python3

class SwimMixin:
    def swim(self):
        print("Swimming...")


class FlyMixin:
    def fly(self):
        print("Flying...")


class Mermaid(SwimMixin):
    def swim(self):
        print("The creature swims!")


class Bird(FlyMixin):
    def fly(self):
        print("The creature flies!")


class SuperCreature(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

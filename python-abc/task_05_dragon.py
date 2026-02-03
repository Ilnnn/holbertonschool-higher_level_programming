class Mermaid(SwimMixin):
    def swim(self):
        print(f"The creature swims!")

class Bird(FlyMixin):
    def fly(self):
        print(f"The creature flies")

class SuperCreature(SwimMixin, FlyMixin):
    def roar(self):
        print(f"The dragon roars!")

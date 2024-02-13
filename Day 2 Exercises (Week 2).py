# Single Inheritence

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("Random Animal Noise")
class Dog(Animal):
    def __init__(self, name, species,):
        super().__init__(name, species)
        print("The", self.species, "says Woof Woof")

Pug = Dog("Jason", "Pug")
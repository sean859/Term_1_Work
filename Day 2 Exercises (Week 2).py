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

# Multiple Inheritence
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Skills:
    def __init__(self, programming_skills, communication_skills):
        self.programming_skills = programming_skills
        self.communication_skills = communication_skills

class Employee(Person, Skills):
    pass


# Multilevel Inheritence

class Vechile:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        print("The engine is starting")

class Car(Vechile):
    def __init__(self, model, year):
        super().__init__(model, year)
        print("The", self.model, "is now driving")

class EletricCar(Car):
    def __init__(self, model, year):
        super().__init__(model, year)
        print("The battery is charging")

randomcar = Car("Mini cooper", 2018)
raandomeletriccar = EletricCar("Tesla", 2023)

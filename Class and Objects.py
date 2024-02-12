# Class Creation

class Car:
    def __init__(self, make, model, year): # Constructor
        self.make = make
        self.model = model
        self.year = year
    def __del__(self): # Deconstructor
        class_name = self.__class__.__name__
        print(class_name, "was removed")
    def give_details(self): # Print Details For Cars
        print("Make:", self.make, "| Model:", self.model, "| Year:", self.year)
    def start_engine(self): # Start the car engine
        print("The engine is starting")

def Car_Stuff():
    My_Car = Car("General Motors", "Chevrolet Corvette", 1985)
    Second_Car = Car("Nissan Motor Company", "Nissan Note", 2018)
    Third_Car = Car("Mazda", "Mazda Axela", 2015)
    My_Car.give_details()
    My_Car.start_engine()
    del My_Car
    Second_Car.give_details()
    Third_Car.give_details()
Car_Stuff()

class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "has been deleted")
    def print_details(self):
        print("Name:", self.fname, self.lname, " | Age:", self.age)

def Person_Stuff():
    Random_Person = Person("Sean", "Albertn", 18)
    Random_Person.print_details()
    del Random_Person
Person_Stuff()

class Task:
    def __init__(self,description):
        self.desc = description
    def cleanup(self):
        print("Task has been completed")
        print("Removing....")
    def __del__(self):
            class_name = self.__class__.__name__
            print(class_name, "was removed")
    def Complete(self):
        print("Your requirments for", self.desc, "have been met")

def Task_Stuff():
    Random_Task = Task("Program all Day 1 Exercises")
    Random_Task.Complete()
    Random_Task.cleanup()
    del Random_Task
Task_Stuff()

class Rectagle:
    def __init__(self, length = 1, width = 1):
        self.length = length
        self.width = width
    def print_square(self):
        print("Length =", self.length, " | Width =", self.width)

Square = Rectagle("150cm", "124cm")
Square.print_square()

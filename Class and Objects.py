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

My_Car = Car("General Motors", "Chevrolet Corvette", 1985)
Second_Car = Car("Nissan Motor Company", "Nissan Note", 2018)
Third_Car = Car("Mazda", "Mazda Axela", 2015)
My_Car.give_details()
My_Car.start_engine()
del My_Car
Second_Car.give_details()
Third_Car.give_details()

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
Random_Person = Person("Sean", "Albertn", 18)
Random_Person.print_details()
del Random_Person
# Class Creation

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def give_details(self):
        print("Make:", self.make, "| Model:", self.model, "| Year:", self.year)
    def start_engine(self):
        print("The engine is starting")

My_Car = Car("General Motors", "Chevrolet Corvette", 1985)
Second_Car = Car("Nissan Motor Company", "Nissan Note", 2018)
Third_Car = Car("Mazda", "Mazda Axela", 2015)
My_Car.give_details()
My_Car.start_engine()
Second_Car.give_details()
Third_Car.give_details()


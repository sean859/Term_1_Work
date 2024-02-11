# Class Creation

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        print("The engine is starting")

My_Car = Car("General Motors", "Chevrolet Corvette", 1985)
Second_Car = Car("Nissan Motor Company", "Nissan Note", 2018)
Third_Car = Car("Mazda", "Mazda Axela", 2015)
print(My_Car.model)
print(My_Car.make)
print(My_Car.year)
print(Second_Car.model)
print(Second_Car.make)
print(Second_Car.year)
print(Third_Car.model)
print(Third_Car.make)
print(Third_Car.year)
My_Car.start_engine()

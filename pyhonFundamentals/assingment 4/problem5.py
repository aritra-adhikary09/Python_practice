'''Concept: Inheritance

Create a base class named Vehicle with attributes such as brand and model.

Then create two subclasses:

Car → adds an extra attribute seats

Bike → adds an extra attribute engine_cc

Use inheritance so that Car and Bike reuse the properties of Vehicle.'''

class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model 
        
    
class Car(Vehicle):
    def __init__(self,brand,model,seats):
        self.seats = seats 
        super().__init__(brand,model)
    def car_brand(self):
        print(f"The brand of this car is {self.brand}.")
    
    def car_model(self):
        print(f"Model no. of this car is {self.model}.")
    
    def no_of_seats(self):
        print(f"This car has {self.seats} seats.")
class Bike(Vehicle):
    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc = engine_cc
    
    def bike_brand(self):
        print(f"The bike is from {self.brand} brand.")

    def bike_model(self):
        print(f"Model No.{ self.model}")
    
    def bike_engine_cc(self):
        print(f"This bike has a engine capacity of {self.engine_cc} CC")
    

car1 = Car("Toyota","345z",7)
bike1 = Bike("Yamaha","classic70",350)

car1.car_brand()




        

        
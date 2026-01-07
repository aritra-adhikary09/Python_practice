'''Concept: Inheritance

Create a base class named Vehicle with attributes such as brand and model.

Then create two subclasses:

Car → adds an extra attribute seats

Bike → adds an extra attribute engine_cc

Use inheritance so that Car and Bike reuse the properties of Vehicle.'''

class Vehicale:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
class Car(Vehicale):
    def __init__(self, brand, model,seats):
        self.seats = seats
        super().__init__(brand, model)
    def car_brand(self):
        return self.brand
    def car_model(self):
        return self.model
    def car_seats(self):
        return self.seats
    
class Bike(Vehicale):
    def __init__(self, brand, model,engine_cc):
        self.engine_cc = engine_cc
        super().__init__(brand, model)

    def bike_brand(self):
        return self.brand
    def bike_model(self):
        return self.model
    def bike_engine_cc(self):
        return self.engine_cc

car = Car("Toyota","I don't know about cars",4)
bike = Bike("Yamaha","idon't about bikes",250)

print(f"This car brand name is {car.brand}") 

print(f"This bike has {bike.engine_cc} cc of enginge.")
    
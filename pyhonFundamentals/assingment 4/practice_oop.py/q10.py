class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model,seats):
        self.seats = seats
        super().__init__(brand, model)

    def Brand_name(self):
        return self.brand
    def Model_name(self):
        return self.model
    def Seat_capacity(self):
        return self.seats

class Bike(Vehicle):
    def __init__(self, brand, model,engine_cc):
        self.engine_cc = engine_cc
        super().__init__(brand, model)
    
    def Brand_name(self):
        return self.brand
    def Model_name(self):
        return self.model
    def Engine_capacity(self):
        return self.engine_cc

car = Car("randomCar","have no idea",100)
bike = Bike("Royal Enfield","huter 650",650)

print(car.Seat_capacity())
print(bike.Engine_capacity())
        
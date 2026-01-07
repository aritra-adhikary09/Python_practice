class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def get_type(self):
        return ("generic Vehicle")
    
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    
    def get_type(self):
        return ("car")    
    def brand_name(self):
        return self.brand
    def model_name(self):
        return self.model

class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def get_type(self):
        return ("bike")
    def brand_name(self):
        return self.brand
    def model_name(self):
        return self.model

bike = Bike("gudchatu","podmarani")
car = Car("Jhatu car","bistality lover")

print(car.get_type())
print(bike.get_type())
        
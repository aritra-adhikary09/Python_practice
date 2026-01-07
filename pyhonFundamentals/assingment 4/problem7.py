'''Q7. Create a class named Person such that its constructor can be used in the following ways:

With name only

With name and age

With name, age, and address

Since Python does not support direct constructor overloading (multiple constructors with different parameters), 
you must use default parameters in the constructor to simulate constructor overloading.'''

class person:
    def __init__(self,name,age=None,address=None):
        self.name = name
        self.age = age
        self.Address = address
    
    def address(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Address:",self.Address)
        print("----------------------")

# KhankiChoda = person("Supratim",)
# KhankiChoda.address()
# BalChera = person("soumen Chowudhary",20)
# BalChera.address()
gudmarani = person("Akash",21,"Sakari Bazar")
gudmarani.address()
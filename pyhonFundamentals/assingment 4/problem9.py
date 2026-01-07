'''Concept: Multiple Inheritance

Q9. Create the following classes:

Herbivore

Carnivore

Omnivore

Each class should have some attributes and methods.

Then, create a class named Bear,
 that inherits from all the above classes to demonstrate how multiple inheritance works in Python.'''

class Herbivore:
    def eat_plants(self):
        print("Eats plants and grass")

class Carnivore:
    def eats_meat(self):
        print("Eats Meat and fish")
    
class Omnivore:
    def eats_both(self):
        print("Eats everything.")

class Bear(Herbivore,Carnivore,Omnivore):
    def __init__(self,name):
        self.name = name
        
bear = Bear("polar Bear")

bear.eat_plants()


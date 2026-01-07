'''Concept: Function Overriding

Create a class Shape with a method area().
Create subclasses Circle, Rectangle, and Triangle that override the area() method.'''

class shape:
    def area(self):
        print("area of shape is not defined!")
    

class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14*(self.radius*self.radius)
    
class Rectangle(shape):
    def __init__(self, length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length*self.width

class Triangle(shape):
    def __init__(self,base,height):
        self.base = base 
        self.height = height
    
    def area(self):
        return 0.5*self.base*self.height
    
c = circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 8)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())
print("Triangle Area:", t.area())

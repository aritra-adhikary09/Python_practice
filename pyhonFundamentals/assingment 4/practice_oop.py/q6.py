'''Concept: Function Overriding

Create a class Shape with a method area().
Create subclasses Circle, Rectangle, and Triangle that override the area() method.'''
# ans
class Shape:
    def area(self):
        print("area of shape is not defined!")

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14*(self.radius*self.radius)
    
class Retangle(Shape):
    def __init__(self,length,widht):
        self.length = length
        self.width = widht

    def area(self):
        return (self.length*self.width)

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5*self.base*self.height
n = int(input("Enter the number: "))    
c = Circle(n)


print("cirecle area:",c.area())

          
        

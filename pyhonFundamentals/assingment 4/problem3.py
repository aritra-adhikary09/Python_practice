'''Create a class named Student with private attributes __name, __roll_no, and __marks.
Provide appropriate getter and setter methods for each attribute.
Implement validation in the setter methods such that:

The name cannot be empty

The roll number must be between 1 and 100

The marks cannot be negative'''

class student:
    def __init__(self,name,roll_no,marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)
    
    def get_name(self):
        return self.__name
    def get_roll_no(self):
        return self.__roll_no
    def get_marks(self):
        return self.__marks
    
    def set_name(self,name):
        if name.strip() == "":
            raise ValueError("Name cannot be empty")
        self.__name = name 
    def set_roll_no(self,roll_no):
        if roll_no<1 or roll_no>100:
            raise ValueError("roll Number must be between 1 and 100")
        self.__roll_no = roll_no
    def set_marks(self,marks):
        if marks <0:
            raise ValueError("marks cannot be negetive")    
        self.__marks = marks

s1 = student("Aritra Adhikary",3,78)
print(s1.get_name())
    
    
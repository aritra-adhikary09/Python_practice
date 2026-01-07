# question written in q4.txt file [please open it to the side pannel]
class Student:
    def __init__(self, name, roll_number, marks):
        self.set_name(name)
        self.set_roll_number(roll_number)
        self.set_marks(marks)

    # ---------- Getters ----------
    def get_name(self):
        return self.__name

    def get_roll_number(self):
        return self.__roll_number

    def get_marks(self):
        return self.__marks

    # ---------- Setters ----------
    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if name.strip() == "":
            raise ValueError("Name must not be empty.")
        if len(name.strip()) < 3:
            raise ValueError("Name must contain at least 3 characters.")
        self.__name = name.strip()

    def set_roll_number(self, roll_number):
        if not isinstance(roll_number, int):
            raise ValueError("Roll number must be an integer.")
        if roll_number < 1 or roll_number > 1000:
            raise ValueError("Roll number must be between 1 and 1000.")
        self.__roll_number = roll_number

    def set_marks(self, marks):
        if not isinstance(marks, (int, float)):
            raise ValueError("Marks must be a number.")
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")
        self.__marks = marks


# ---------- Testing ----------
try:
    student1 = Student("Aritra Adhikary",34,79)
    print(student1.get_name())
    student1.set_name(34)
except ValueError as e:
    print(e)

try:
    student1.set_marks("aritra")
    print(student1.get_marks())
except ValueError as f:
    print(f)

try:
    student1.set_roll_number(100)
    print(student1.get_roll_number())
except ValueError as g:
    print(g)


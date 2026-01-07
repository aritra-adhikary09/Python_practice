'''Create an abstract class named Employee that contains an abstract method called calculate_salary().

Then, create three subclasses:

Intern

FullTimeEmployee

ContractEmployee

Each subclass must implement the calculate_salary() method in a different way,
based on how that type of employee is paid.'''
# ans
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass 

class Intern(Employee):
    def __init__(self,stipend):
        self.stipend = stipend
    
    def calculate_salary(self):
        return self.stipend

class FullTimeEmployee(Employee):
    def __init__(self,salary):
        self.salary = salary
    
    def calculate_salary(self):
        return self.salary

class ContractEmployee(Employee):
    def __init__(self,hourly_rate,hours_worked):
        self.hourlyRate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        return self.hourlyRate*self.hours_worked

intern = Intern(6000)
FullTimeEmployee1 =FullTimeEmployee(70000)
ContractEmployee1 =ContractEmployee(3,67)

print(intern.calculate_salary())
print(FullTimeEmployee1.calculate_salary())
print(ContractEmployee1.calculate_salary())
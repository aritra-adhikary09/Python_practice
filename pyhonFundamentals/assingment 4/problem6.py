'''Create an abstract class named Employee that contains an abstract method called calculate_salary().

Then, create three subclasses:

Intern

FullTimeEmployee

ContractEmployee

Each subclass must implement the calculate_salary() method in a different way,
based on how that type of employee is paid.'''

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def  calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self,stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend
    

class FullTimeEmployee(Employee):
    def __init__(self,monthlyPay):
        self.monthlyPay = monthlyPay
    
    def calculate_salary(self):
        return self.monthlyPay
    

class ContractEmployee(Employee):
    def __init__(self,hourly_rate,hours_worked):
        self.hourlyRate = hourly_rate
        self.HoursWorked = hours_worked
    
    def calculate_salary(self):
        return self.hourlyRate*self.HoursWorked


intern = Intern(8000)    
fullTimeEmployee = FullTimeEmployee(100000)
contract_employee = ContractEmployee(100,6)

print(f"Intern Salary: {intern.calculate_salary()}")
print(f"Fulltime Employee salary: {fullTimeEmployee.calculate_salary()}")
print(f"Contract Employees Salary: {contract_employee.calculate_salary()}")
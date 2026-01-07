class Employee:
    def calculate_salary(self):
        return 0

class FullTImeEmployee(Employee):
    def __init__(self,amount):
        self.amount = amount
    
    def calculate_salary(self):
        return self.amount

class PartTimeEmployee(Employee):
    def __init__(self,hourly_rate,hours_worked):
        self.hourly_rate = hourly_rate
        self.hourly_worked = hours_worked
    
    def calculate_salary(self):
        return self.hourly_rate*self.hourly_worked
    
class Intern(Employee):
    def __init__(self,stipend):
        self.stipend = stipend
    
    def calculate_salary(self):
        return self.stipend

employees = [FullTImeEmployee(60_000),
            PartTimeEmployee(192,200),
            Intern(12000)]
for emp in employees:
    print(emp.calculate_salary())


        
    
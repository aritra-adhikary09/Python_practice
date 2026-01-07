'''Create a dictionary where:
• Keys = student names
• Values = marks (integer)
Write a menu-based program where user presses a key (’A’, ‘B’, ‘C’, ‘D’)
depending on the operation they want to perform on the dictionary:
1. A - Add a student
2. B - Update marks
3. C - Search for a student
4. D - Display all students and marks'''

a = {"Aritra":92,
     "santanu":98,
     "riku":90, 
     "bikram":78
     }

b = input('''
1. A - Add a student
2. B - Update marks
3. C - Search for a student
4. D - Display all students and marks

What task you want to perform form above options?
Your input: ''')


while True:
     if b == "A":
          student = input("Enter the student name:")
          marks = int(input("Enter marks of the student: "))
          a.update({student:marks})
          print("New updated dictionary:",a.items())

     elif b == "B":
          student = input("Enter student name to update: ")
          marks = int(input("Enter the marks to update: "))
          a[student] = marks
          print("New updated dictionary:",a.items())

   
     elif b == "C":
          stu_name = input("Enter the student name: ")
          # checks if any key exist in a dictionary same as the student name
          marks = a.get(stu_name)
          # .get(key) gives either the value, or None if key doesn't exist
          while not marks: # if marks is None
               print("Invalid input, please enter a correct name")
               stu_name = input("Enter the student name: ")
               marks = a.get(stu_name)
          print("Marks", marks)
        
           

     elif b == "D":
          print(a.items())

     else:
          print("Wrong input!! Try again....")
          b = input('''
1. A - Add a student
2. B - Update marks
3. C - Search for a student
4. D - Display all students and marks

What task you want to perform form above options?
Your input:
                     ''')
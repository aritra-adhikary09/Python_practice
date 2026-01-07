'''Q3. Create a Python program that:

Contains a list of numbers:
[5, 10, 15, 20, 25]

Uses a list comprehension to create a new list that includes only the numbers greater than 15

Prints the new list'''
# ans:
list = [5, 10, 15, 20, 25]

a= [i for i in list if i > 15]

print(a)
    

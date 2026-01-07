'''Write a program to find the sum of the digits of a number n.
Example: n = 524 → 5 + 2 + 4 = 11'''
n = int(input("Enter the number: "))

sum = 0

while n>0:
    sum = sum+(n%10)
    n = n//10

print("sum:",sum)
    
    
   


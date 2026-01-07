'''Reverse a number
Print the number n in reverse order.
Example: n = 1234 → 4321'''

n = int(input("Enter the number: "))

rev = 0

while n>0 :
    rev = rev*10+(n%10)
    n =n//10

print(rev)
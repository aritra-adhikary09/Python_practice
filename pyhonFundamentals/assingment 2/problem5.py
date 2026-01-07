'''Write a function to return the sum of digits of a number, n'''

n = int(input("Enter the number: "))

digit = 0

def Sum_num(n):
    while n>0:
        digit += n%10

        n//= 10
    return digit

print(Sum_num(n))


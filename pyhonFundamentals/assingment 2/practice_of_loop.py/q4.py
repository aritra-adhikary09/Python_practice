'''
Calculate the product of all digits in a number n.
Example: n = 234 → 2 × 3 × 4 = 24'''

n = int(input("Enter the number: "))

b = 1

while n>0:
    b *= n%10

    n= n//10

print("Product of all digits: ",)
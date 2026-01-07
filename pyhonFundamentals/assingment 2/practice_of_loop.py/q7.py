'''Find the smallest digit
Example: n = 50429 → smallest = 0'''

n = int(input("Enter number: "))
smallest = 9

while n > 0:
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n = n // 10

print("Smallest digit:", smallest)

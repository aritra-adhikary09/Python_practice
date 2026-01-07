'''Write a program that finds the largest digit in the number n.
Example: n = 38597 → largest = 9'''

n = int(input("Enter number: "))
largest = 0

while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n = n // 10

print("Largest digit:", largest)



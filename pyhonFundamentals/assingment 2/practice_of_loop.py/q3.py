'''Given a number n, count how many digits it contains.
Example: n = 8907 → 4 digits'''

n = int(input("Enter the number: "))

dgt = 0

while n>0:
    dgt += 1

    n=n//10

print(dgt)
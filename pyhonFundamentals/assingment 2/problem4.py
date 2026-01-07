# Write a function to return the count the number of digits in a number, n .

def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10    # remove the last digit
        count += 1     # increase count
    return count

# Example:
print(count_digits(312))   # Output: 3

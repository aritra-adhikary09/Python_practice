# Given a list of integers compute the average of all numbers in the list.

numbers = [1,2,3,4,5,6,7,8,9,10]   # example list

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print("Average:", average)

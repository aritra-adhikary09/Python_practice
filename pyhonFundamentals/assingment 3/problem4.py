'''Given a tuple of integers, create: 
• A tuple of all even numbers 
• A tuple of all odd numbers'''

numbers = tuple(map(int,input("Enter numbers: ")))
even = []
odd = []
for nums in numbers:
    if nums %2 == 0:
        even.append(nums)
    else:
        odd.append(nums)
even = tuple(even)
odd = tuple(odd)

print(even)
print(odd)
# Input two lists of integers from the user. Merge them into one list and sort the result.

list1 = list(map(int, input("Enter numbers for list1 separated by space: ")))
list2 = list(map(int, input("Enter numbers for list2 separated by space: ")))

result = list1 + list2
result.sort()

print("Merged & Sorted List:", result)



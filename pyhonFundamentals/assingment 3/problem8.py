''' Write a program to check whether two lists share no common elements.
# share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# share common elements list1 = [1, 2, 3] list2 = [3, 4]
[Hint - use sets]'''

list1 = list(map(int,input("Enter the list elements: ").split()))
list2 = list(map(int,input("Enter the list elements: ").split()))

set1 = set(list1)
set2 = set(list2)

if set1.intersection(set2):
    print("They share common elements:", set1.intersection(set2))
else:
    print("They share NO common elements.")



'''Given a list, print all elements that appear more than once in the list.
[Hint - use sets]'''
lst = [1, 2, 3, 2, 4, 5, 1, 6, 3]

seen = set()          # keeps track of elements we see
duplicates = set()    # keeps track of elements appearing more than once

for i in lst:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)
    
    
print(duplicates)

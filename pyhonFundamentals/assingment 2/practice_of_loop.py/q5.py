'''A palindrome reads the same backward and forward.
Example: n = 121 → palindrome'''

n = int(input("Enter the number: "))

d = n

rev = 0

while d>0:
    rev = rev*10 + (d%10)
    
    d //= 10

if rev==n:
    print(rev,"is a palindrome digite")
else:
    print(rev,"none")
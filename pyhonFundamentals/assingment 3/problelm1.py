# Ask the user for a string and check whether it is a palindrome or not.

palindrome = input("Enter your word: ")

if palindrome == palindrome[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")

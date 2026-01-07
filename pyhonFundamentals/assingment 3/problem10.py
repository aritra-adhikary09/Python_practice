'''Ask the user for a string and print:
• All unique characters
• The count of unique characters
'''

ask_user = input("Enter anything: ")

ask_user = set(ask_user) 
# just use set get unique characters
print(ask_user)
print(len(ask_user))



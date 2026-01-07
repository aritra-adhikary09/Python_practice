'''Write a Python program that tries to open a file called data.txt in read mode.
If the file does not exist, handle the error properly and print:
File not found!'''
# answer: 
try:
    file = open("data.txt", "r")
    # You can read the file if needed
    file.close()
except FileNotFoundError:
    print("File not found!")

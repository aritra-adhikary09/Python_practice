'''Design a program to continuously input a number n from user & print if it is
positive or negative until the user enters “Quit”.'''

# while True:
#     user_input = input("Enter a number (or type 'quit' to stop): ")
#     if (user_input == "quit"):
#         print("The program ended")
#         break
#     n = float(user_input)

#     if n>0:
#         print("positive number")
#     elif n<0:
#         print("negetive number")
#     else:
#         print("Zero")

while True:
    user_input = input("Enter a number (or type 'Quit' to stop): ")

    if user_input == "Quit":
        print("Program ended.")
        break

    n = float(user_input)   # convert input to number

    if n > 0:
        print("Positive number")
    elif n < 0:
        print("Negative number")
    else:
        print("Zero")

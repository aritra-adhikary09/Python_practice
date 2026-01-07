'''Q10. Let’s create a “Number Guessing Game”.
Given a secret number (already decided by you), write a program that asks the user to guess it and prints:

"Too high" if the guess is above the number

"Too low" if the guess is below

"Correct!" if the guess matches'''


secret_number = 7  # you can choose any number you like

guess = int(input("Guess the number: "))

if guess > secret_number:
    print("Too high")
elif guess < secret_number:
    print("Too low")
else:
    print("Correct!")

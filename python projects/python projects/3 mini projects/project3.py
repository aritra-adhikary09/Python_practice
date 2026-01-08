# password gussing game
import random

easy_words = ["tom","jerry","omega3","cellular data","comdom","pen"]
medium_words = ["stand up comedy","calligraphy","v-tubers","primogems","hololive"]
hard_words = ["welcome","anime","genshin impact","wuwa","japan","bukky mouse","india","jai sri ram"]

print("Welcome to the password geussing game")
print("Choose a difficulty level: easy, medium, hard")

level = input("Enter difficulty level: ").lower().strip()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium" :
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defulting to easy level")
    secret = random.choice(easy_words)

attempts = 0
print("Guess the secter passwords")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1
    if guess == secret:
        print(f"congratulations! you guessed it in {attempts} attempts.")
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint: " + hint)

print("Game Over.")
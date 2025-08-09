import random
secret_number = random.randint(1, 10)
guess_number = int(input("Enter your guess number, 1- 10:"))
if guess_number >= secret_number:
    print("Guess number is high, try again!")
elif guess_number <= secret_number:
    print("Guess number is low, try again!")
else:
    print(guess_number)

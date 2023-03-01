import random

def play():
    random_number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        if guess == random_number:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            play_again()
            break
        elif guess < random_number:
            print("The number is higher.")
        else:
            print("The number is lower.")

def play_again():
    response = input("Do you want to play again? (y/n) ")
    if response == "y":
        play()

print("Welcome to the number guessing game.")
play()

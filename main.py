# Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
import random

print(logo)

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# Get a Random Number between 1 and 100
number_to_guess = random.randint(1, 100)
# Levels
EASY_LEVEL = 10
HARD_LEVEL = 5


def set_game_level():
    """Returns the number of turns the player has depending on the level."""
    if game_level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def check_guess(guess, turns):
    """Checks the guess against the user's attempt"""
    if guess == number_to_guess:
        print(f"You guess the number {number_to_guess}")
        turns = -1
    elif guess > number_to_guess:
        print("Too High.")
        turns -= 1
    else:
        print("Too Low.")
        turns -= 1

    return turns


# print(f"Psst. {number_to_guess}")
# Let the user choose the difficulty of the gam
game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
number_of_attempts = set_game_level()

# Ask for guess number if the user has still turns
while number_of_attempts > 0:
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    # Allow the user to make an attempt
    my_guess = int(input("Make a guess: "))
    number_of_attempts = check_guess(my_guess, number_of_attempts)


if number_of_attempts == 0:
    print("You've run out of guesses, you lose")


## Numbers guessing game project

import random
from art import day12

def user_guess_check(user_guess_p):
    if user_guess_p == random_num:
        print(f"You Guessed Correctly, the answer was {random_num} you Won! 😀💃🏽")
    elif user_guess_p < random_num:
        print("Too Low")
    else:
        print("Too high")


def easy_level():
    print("You only have 10 attempts to guess the number")
    number_guess = 10
    user_guess = int(input("Make a guess: "))
    user_guess_check(user_guess)
    game_still_on = True
    while user_guess != random_num and game_still_on:
        number_guess -= 1
        print(f"You only have {number_guess} left ")
        user_guess = int(input("Make a guess: "))
        user_guess_check(user_guess)
        if number_guess == 0:
            print(f"You Lose 😭, you are out of attempts! The correct answer was {random_num}")
            game_still_on = False

def hard_level():
    print("You only have 5 attempts to guess the number")
    number_guess = 5
    user_guess = int(input("Make a guess: "))
    user_guess_check(user_guess)
    game_on = True
    while user_guess != random_num and game_on:
        number_guess -= 1
        print(f"You only have {number_guess} left ")
        user_guess = int(input("Make a guess: "))
        user_guess_check(user_guess)
        if number_guess == 0:
            print(f"You Lose 😭, you are out of attempts! The correct answer was {random_num}")
            game_on = False



print(day12)
print("Welcome to the Number Guessing Game!")
random_num = random.randint(0,100)
print("I am thinking of a whole number between 1 and 100.")
user_level = input("Choose a difficultly level. Type 'easy' or 'hard': ").lower()
if user_level == 'easy':
    easy_level()
elif user_level == 'hard':
    hard_level()
else:
    print("You didn't select correctly")



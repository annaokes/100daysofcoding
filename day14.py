from dataforday14 import data
import random
import os
from art import  day14v1,day14v2
score = 0
def game_on():
    global rand_person, second_person, score, user_choice
    game_continues = True
    while game_continues:
        if user_choice == 'A' and rand_person['follower_count'] > second_person['follower_count']:
            score += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Well done that is correct, your current score is: {score}')
            print(f"Compare A: {rand_person['name']}, who has {rand_person['follower_count']} million followers ,{rand_person['description']}, from {rand_person['country']}")
            print(day14v2)
            second_person = random.choice(data)
            print(f"With Option B: {second_person['name']}, {second_person['description']}, from {second_person['country']}")
            user_choice = input("Who has the highest followers? Type 'A' or 'B': ").upper()
        elif user_choice == 'B' and second_person['follower_count'] > rand_person['follower_count']:
            score += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Well done that is correct, your current score is: {score}')
            rand_person = second_person
            print(f"Compare A: {rand_person['name']}, who has {rand_person['follower_count']} million followers ,{rand_person['description']}, from {rand_person['country']}")
            print(day14v2)
            second_person = random.choice(data)
            print(f"With Option B: {second_person['name']}, {second_person['description']}, from {second_person['country']}")
            user_choice = input("Who has the highest followers? Type 'A' or 'B': ").upper()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Sorry that is incorrect the game ends, your final score is {score}")
            game_continues = False



print(day14v1)
rand_c = random.choice(data)
rand_person = rand_c
print(f"Compare A: {rand_person['name']}, who has {rand_person['follower_count']} million followers, {rand_person['description']}, from {rand_person['country']}")
print(day14v2)
second_person = random.choice(data)
print(f"With Option B: {second_person['name']}, {second_person['description']}, from {second_person['country']}")
user_choice = input("Who has the highest followers? Type 'A' or 'B': ").upper()

game_on()


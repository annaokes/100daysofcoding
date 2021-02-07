### ROCK PAPER SCISSORS GAME
import random
print("Hey, welcome to Rock, Paper, Scissors!!")

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
player_choice = int(player_choice)

if player_choice == 0:
    print("You chose rock")
    print ('''
        _______
     ---'   ____)
           (_____)
          (_____)
          (____)
    ---.__(___)
    ''')


elif player_choice == 1:
    print("You chose paper")
    print('''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    ''')

elif player_choice == 2:
    print("You chose scissors")
    print(''' 
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')
computer_choice = random.randint(0,2)

if computer_choice == 0:
    print("The computer picked rock")
    print ('''
        _______
     ---'   ____)
           (_____)
          (_____)
          (____)
    ---.__(___)
    ''')


elif computer_choice == 1:
    print("The computer picked paper")
    print('''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    ''')

elif computer_choice == 2:
    print("The computer picked scissors")
    print(''' 
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')


if player_choice == 0 and computer_choice == 2:
    print("You WIN 🏆 ")
elif player_choice == 1 and computer_choice == 0:
    print("You WIN 🏆 ")
elif player_choice == 2 and computer_choice==1:
    print("You WIN 🏆 ")
elif player_choice==computer_choice:
    print("Its a draw ‼️")
else:
    print("You LOSE 😞 ")

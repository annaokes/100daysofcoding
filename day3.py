## Building a game project

print('''
 _n_________________
|_|_______________|_|
|  ,-------------.  |
| |  .---------.  | |
| |  |         |  | |
| |  |         |  | |
| |  |         |  | |
| |  |         |  | |
| |  `---------'  | |
| `---------------' |
|   _ GAME BOY      |
| _| |_         ,-. |
||_ O _|   ,-. "._,"|
|  |_|    "._,"   A | 
|    _  _    B      | 
|   // //           |
|  // //    \\\\\\  |
|  `  `      \\\\\\ ,
|________...______,"
''')

print("Welcome to Anna's Treasure Game :) \nThe Mission of this game is to find the treasure, using various commands")

print("Setting the scene....\nYou are in a deserted corridor, there are two doors, one to your left and the other to your right")

first_command = input("Please pick a choice to go left or right?: ")
first_command = first_command.lower()

if first_command == 'left':
  print("You picked left, you are now walking cautiously to the left and before you know it, \nyou realised you've reached the end of the walkway path,\n you now have two options to either swim or wait for someone")
  second_command = input("Please decide if you want to swim or wait?: ")
  second_command=second_command.lower()
  if second_command == 'wait':
    print("Welp, you survived a scare there, now onto the final challenge. \nThis door separates you from achieving the game objective. \n What colour door are you picking?")
    third_command = input("Please select a door colour: Red, Blue or Yellow: ")
    third_command=third_command.lower()
    if third_command == 'yellow':
      print("YOU'VE WON!!!!!!!!")
      print('''
        ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
             `"""""""`
             ''')
    else:
      print("GAME OVER")
  else:
    print("GAME OVER")
else:
  print("GAME OVER!")

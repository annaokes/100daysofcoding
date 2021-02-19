from turtle import Turtle, Screen
import random
import turtle as turtle_module


screen = Screen()

screen.setup(width=500, height=400)

colours = ["red", "yellow", "purple", "green", "orange", "blue"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

turtle_module.bgcolor("MediumSeaGreen")

for turtle_index in range(0,6):
    turtle_race = Turtle(shape='turtle')
    turtle_race.color(colours[turtle_index])
    turtle_race.penup()
    turtle_race.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(turtle_race)

finish_line = Turtle()
finish_line.penup()
finish_line.goto(x=225,y=0)
finish_line.pendown()
finish_line.pensize(10)
finish_line.pencolor("white")
finish_line.left(270)
finish_line.forward(80)
finish_line.left(180)
finish_line.forward(180)
finish_line.hideturtle()

finish_line_text = Turtle()
finish_line_text.penup()
finish_line_text.goto(x=160,y=105)
finish_line_text.pendown()
style = ('Courier', 20, 'italic')
finish_line_text.color("white")
finish_line_text.write("Finish", font=style)
finish_line_text.hideturtle()

style_2 = ('Courier', 15, 'bold')

def winner():
    global style
    you_win = Turtle()
    you_win.penup()
    you_win.goto(x=-100,y=190)
    you_win.hideturtle()
    you_win.write("You WIN!", font=style_2)


def loser():
    global style
    you_lose = Turtle()
    you_lose.penup()
    you_lose.goto(x=-100,y=160)
    you_lose.hideturtle()
    you_lose.write("SOZ You Lost!", font=style_2)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour:").lower()
if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 210:
            winning_colour = turtle.pencolor()
            is_race_on = False
            if winning_colour == user_bet:
                winner()
            else:
                loser()
        random_moves = random.randint(0,10)
        turtle.forward(random_moves)

screen.exitonclick()
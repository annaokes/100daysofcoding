from turtle import Turtle, Screen
from players_day23 import Players
from ball_day23 import Ball
from score_day23 import Scoreboard
import time


screen = Screen()
screen.bgcolor("grey")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

line = Turtle()

for i in range(100):
    line.penup()
    line.color("white")
    line.goto(x=0,y=270)
    line.pendown()
    line.setheading(270)
    line.forward(600)




right_player = Players((350,0))
left_player = Players((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_player.go_up, "Up")
screen.onkey(right_player.go_down, "Down")

screen.onkey(left_player.go_up, "w")
screen.onkey(left_player.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #Detect wall collision
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect paddle collision
    if ball.xcor() > 320 and ball.distance(right_player) < 50 or ball.xcor() < -320 and ball.distance(left_player) < 50:
        ball.bounce_x()

    # Detect out of bounds
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.left_score()

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.right_score()




screen.exitonclick()


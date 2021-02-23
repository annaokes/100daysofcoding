from turtle import Turtle
import random

STARTING_SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.x_move = STARTING_SPEED
        self.y_move = STARTING_SPEED
        self.move_speed = 0.1


    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.7

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
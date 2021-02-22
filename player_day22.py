from turtle import Turtle
STARTING_POSITION = (0, -280)
FINISH_LINE = 280
MOVE = 10

class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.setheading(90)
        self.forward(MOVE)

    def go_left(self):
        self.setheading(180)
        self.forward(MOVE)

    def go_right(self):
        self.setheading(0)
        self.forward(MOVE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)












from turtle import Turtle


class Players(Turtle):
    def __init__(self,position):
        super(Players, self).__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.penup()
        self.color("white")
        self.goto(position)


#self in here calls anything created above here to do stuff

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




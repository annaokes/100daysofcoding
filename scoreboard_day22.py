from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f'Level : {self.level}', align='left', font=("Courier",24,"bold"))


    def gameover(self):
        self.goto(0,0)
        self.write('GAME OVER!! ', align='center', font=("Courier", 24, "bold"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
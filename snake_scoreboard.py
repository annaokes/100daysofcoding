from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f'Score : {self.score}', align='center', font=("Courier",24,"bold"))


    def gameover(self):
        self.goto(0,0)
        self.write('GAME OVER!! ', align='center', font=("Courier", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()









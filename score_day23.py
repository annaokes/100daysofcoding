from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.right_player = 0
        self.left_player = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(-380,270)
        self.write(f'score : {self.left_player}', align='left', font=("Courier",24,"bold"))
        self.goto(250,270)
        self.write(f'score : {self.right_player}', align='left', font=("Courier",24,"bold"))
        self.goto(0,270)
        self.write('Classic Ping Pong', align='center', font=("Courier",24,"bold"))


    def left_score(self):
        self.left_player += 1
        self.clear()
        self.update_scoreboard()

    def right_score(self):
        self.right_player += 1
        self.clear()
        self.update_scoreboard()

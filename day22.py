import time
from turtle import Screen, Turtle
from player_day22 import Player
from car_manager_day22 import CarManager
from scoreboard_day22 import Scoreboard

screen = Screen()
screen.bgcolor("grey")
screen.setup(width=600, height=600)
screen.tracer(0)

player_one = Player()
car_creator = CarManager()
score_count = Scoreboard()

screen.listen()
screen.onkey(player_one.go_up, "Up")
screen.onkey(player_one.go_left, "Left")
screen.onkey(player_one.go_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_creator.create_vehicle()
    car_creator.move_cars()
    score_count.update_scoreboard()

    for car in car_creator.all_cars:
        if car.distance(player_one) < 20:
            game_is_on = False
            score_count.gameover()

    if player_one.xcor() > 280 or player_one.xcor() < -280 or player_one.ycor() > 280 or player_one.ycor() < -280:
        player_one.go_to_start()
        car_creator.level_up()
        score_count.increase_level()


screen.exitonclick()


from turtle import Turtle, Screen
import random
screen = Screen()

colours = ["red", "yellow", "purple", "green", "orange", "blue"]
objects = ["square", "triangle", "circle"]
y_positions = random.randint(-250, 250)
x_positions = random.randint(-280, 280)
STARTING_MOVE_DISTANCE = 10
MOVE_INCREASE = 20


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_vehicle(self):
        random_chance = random.randint(1,3)
        if random_chance == 1:
            new_car = Turtle(random.choice(objects))
            new_car.shapesize(stretch_len=1)
            new_car.penup()
            new_car.color(random.choice(colours))
            new_car.goto(320,random.randint(-250,250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor() < -320 or car.xcor() > 320:
                self.all_cars.remove(car)

    def level_up(self):
        self.car_speed += MOVE_INCREASE


















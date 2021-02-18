from turtle import Turtle
import random
import turtle as turtle_module


turtle_module.colormode(255)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
    , "purple2", "tomato", "yellow", "tan3", "red4", "OrangeRed", "DodgerBlue", "gold1", "goldenrod4"]

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)



# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for i in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
# for shape_side in range (3,11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shape(shape_side)

# RANDOM WALK
# directions = [0, 90, 180, 270]
# timmy_the_turtle.speed("fastest")
#
#
# for i in range(300):
#     timmy_the_turtle.pensize(5)
#     timmy_the_turtle.color(random.choice(colours))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))

#SPIROGRAPH
# timmy_the_turtle.speed("fastest")
# for i in range(200):
#     timmy_the_turtle.circle(100)
#     timmy_the_turtle.color(random.choice(colours))
#     current_heading = timmy_the_turtle.heading()
#     timmy_the_turtle.setheading(current_heading+5)
#
from turtle import Turtle
import random
import turtle as turtle_module


turtle_module.colormode(255)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
    , "purple2", "tomato", "yellow", "tan3", "red4", "OrangeRed", "DodgerBlue", "gold1", "goldenrod4"]

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")


#ArtWork
timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)
number_of_dots = 100
timmy_the_turtle.speed("fastest")

for dot_count in range(1,number_of_dots+1):
    turtle_module.bgcolor(random.choice(colours))
    timmy_the_turtle.dot(20,random.choice(colours))
    timmy_the_turtle.forward(50)
    if dot_count % 10 == 0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(50)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(500)
        timmy_the_turtle.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
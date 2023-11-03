# different shapes
from turtle import Turtle, Screen
# import random
from random import randint

screen = Screen()
timmy_the_turtle = Turtle()

screen.colormode(255)
timmy_the_turtle.shape("classic")
timmy_the_turtle.color("red")
timmy_the_turtle.home()

while _:
    timmy_the_turtle.listen()

timmy_the_turtle.penup()
screen.exitonclick()
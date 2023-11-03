# different shapes
from turtle import *
# import random
from random import randint

screen = Screen()
timmy_the_turtle = Turtle()

def ttt_setup():
    screen.colormode(255)
    timmy_the_turtle.shape("classic")
    timmy_the_turtle.color("red")
    timmy_the_turtle.home()
    timmy_the_turtle.pendown()
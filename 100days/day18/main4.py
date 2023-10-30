# different shapes
from turtle import Turtle, Screen
# import random
from random import randint

screen = Screen()
timmy_the_turtle = Turtle()

screen.colormode(255)
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
long = 70

def triangle(sides, long):
    # angles
    angle = 180/sides
    for _ in range(sides):
        timmy_the_turtle.forward(long)
        timmy_the_turtle.right(180-angle)

def square(sides, long):
    long += 5
    for _ in range(4):
        timmy_the_turtle.forward(long)
        timmy_the_turtle.right(90)

def polygon(sides, long):
    long += 5
    angle = (180*(sides-2))/sides
    for _ in range(sides):
        timmy_the_turtle.forward(85)
        timmy_the_turtle.right(180-angle)

for i in range(3, 10):
    # random color
    timmy_the_turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    timmy_the_turtle.pendown()
    long += 5
    if i == 3:
        triangle(i, long)
    elif i == 4:
        square(i, long)
    elif i > 4:
        polygon(i, long)

timmy_the_turtle.penup()
screen.exitonclick()
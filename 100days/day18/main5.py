# different shapes
from turtle import Turtle, Screen
# import random
from random import randint

screen = Screen()
timmy_the_turtle = Turtle()

screen.colormode(255)
timmy_the_turtle.shape("classic")
timmy_the_turtle.color("red")
long = 0
# random color
#timmy_the_turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
timmy_the_turtle.pen(pensize=10)
timmy_the_turtle.pendown()


for i in range(150):
    timmy_the_turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    long = 20 #randint(1, 40)
    angle = randint(1, 360)
    direction = randint(1,100)
    run = randint(1,100)
    if direction > 50:
        timmy_the_turtle.right(angle)
    else:
        timmy_the_turtle.left(angle)
    if run > 50:
        timmy_the_turtle.forward(long)
    else:
        timmy_the_turtle.backward(long)

timmy_the_turtle.penup()
screen.exitonclick()
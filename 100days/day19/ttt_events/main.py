# according to https://realpython.com/python-application-layouts/
from helpers import screen, timmy_the_turtle, ttt_setup

ttt_setup()

# events definitions
def move_forwards():
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)

def move_backwards():
    timmy_the_turtle.backward(10)

def turn_left():
    new_heading = timmy_the_turtle.heading() + 10
    timmy_the_turtle.setheading(new_heading)

def turn_right():
    new_heading = timmy_the_turtle.heading() - 10
    timmy_the_turtle.setheading(new_heading)

def clear():
    timmy_the_turtle.penup()
    timmy_the_turtle.clear()
    timmy_the_turtle.home()
    timmy_the_turtle.pendown()

# just listen to events
screen.listen()

# events triggers
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")

# closing  eveything
timmy_the_turtle.penup()
screen.exitonclick()
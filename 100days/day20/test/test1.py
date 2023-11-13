from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# create snake body
arr_turtles = []
for i in range(3):
    timmy = Turtle(shape="square")
    timmy.color("white")
    timmy.forward(20*i)
    arr_turtles.append(timmy)


# closing  eveything
screen.exitonclick()
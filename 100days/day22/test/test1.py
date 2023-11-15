from turtle import Screen, Turtle

screen = Screen()
# constants are in main
WORLD_WIDTH  = 800
WOLRD_HEIGHT = 600
WORLD_XPOS   = WORLD_WIDTH/2
WORLD_XNEG   = -WORLD_XPOS
WORLD_YPOS   = WOLRD_HEIGHT/2
WORLD_YNEG   = -WORLD_YPOS
# setup
screen.setup(width=WORLD_WIDTH, height=WOLRD_HEIGHT)
screen.bgcolor("black")
screen.title("PONG Game")

# create screen
timmy = Turtle()
timmy.color("white")
timmy.hideturtle()
timmy.penup()
timmy.goto([0,WORLD_YPOS])
timmy.pensize(5)
timmy.right(90)
for _ in range(20):
    timmy.pendown()
    timmy.forward(20)
    timmy.penup()
    timmy.forward(10)

# closing  eveything
screen.exitonclick()
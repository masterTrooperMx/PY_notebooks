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


# closing  eveything
screen.exitonclick()
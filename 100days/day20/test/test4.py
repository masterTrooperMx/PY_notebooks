from turtle import Screen, Turtle
import time

screen = Screen()
arr_turtles = []
keep_running = True

def setupScreen():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

# create snake body
def createSnakeBody():
    for i in range(3):
        timmy = Turtle(shape="square")
        timmy.color("white")
        timmy.penup()
        timmy.forward(20*i)
        arr_turtles.append(timmy)

# moving snake
def turnUp():
    arr_turtles[0].setheading(90)

def turnDown():
    arr_turtles[0].setheading(270)

def turnLeft():
    arr_turtles[0].setheading(180)

def turnRight():
    arr_turtles[0].setheading(0)

screen.listen()

screen.onkey(turnUp, 'Up')
screen.onkey(turnDown, 'Down')
screen.onkey(turnLeft, 'Left')
screen.onkey(turnRight, 'Right')

# do_move
def doMove():
    # move snake
    while keep_running:
        screen.update()
        time.sleep(0.1)
        for t in reversed(arr_turtles):
            ind = arr_turtles.index(t)
            timmy = t
            if ind > 0:
                timmy_bef = arr_turtles[ind-1]
                timmy.goto(timmy_bef.pos())
                #print(f"{ind} {ind-1}")
            else:
                #print(f"{ind}-f")
                timmy.forward(15)
                #timmy.left(45)
            #print(arr_turtles.index(t))

# init
setupScreen()
createSnakeBody()

doMove()

# closing  eveything
screen.exitonclick()
from turtle import Screen, Turtle
import random
import time

screen = Screen()

# constants are in main
WORLD_WIDTH  = 800
WOLRD_HEIGHT = 600
WORLD_XPOS   = WORLD_WIDTH/2
WORLD_XNEG   = -WORLD_XPOS
WORLD_YPOS   = WOLRD_HEIGHT/2
WORLD_YNEG   = -WORLD_YPOS
DELTA        = 10
# setup
screen.setup(width=WORLD_WIDTH, height=WOLRD_HEIGHT)
screen.bgcolor("black")
screen.title("PONG Game")

# create ball
class Ball(Turtle):
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.angle = -1
        
    def setupBall(self):
        if self.angle < 0:
            self.angle = random.randint(0, 89) # where to go
        else:
            # bounce, complementary angle
            self.angle = -1 * self.angle
        self.setheading(self.angle)

    def moveBall(self):
        keep_going = True
        self.setupBall() # turn angle
        time.sleep(0.1)
        while keep_going:
            (t_x, t_y) = self.pos()
            if t_y < WORLD_YPOS-DELTA and t_y > WORLD_YNEG+DELTA:
                self.forward(DELTA)
            else:
                #print(self.pos(), self.angle)
                self.setupBall() #bounce
                self.forward(DELTA)

ball = Ball()
ball.moveBall()


# closing  eveything
screen.exitonclick()
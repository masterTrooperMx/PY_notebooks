from Classes.config import *
from turtle import Turtle
import random
import time

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
    
    def move(self):
        (t_x, t_y) = self.pos()
        if t_y < Pong.WORLD_YPOS-1.5*Pong.DELTA and t_y > Pong.WORLD_YNEG+1.5*Pong.DELTA:
            self.forward(Pong.DELTA)
        else:
            #print(self.pos(), self.angle)
            self.setupBall() #bounce
            self.forward(Pong.DELTA)
        
    def moveBall(self):
        keep_going = True
        self.setupBall() # turn angle
        time.sleep(0.1)
        while keep_going:
            (t_x, t_y) = self.pos()
            if t_y >= Pong.WORLD_YNEG+Pong.DELTA:
                self.forward(Pong.DELTA)
            else:
                self.setupBall() #bounce
                self.forward(Pong.DELTA)

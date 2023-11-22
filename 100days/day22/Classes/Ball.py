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
        (self.t_x, self.t_y) = self.pos()
        self.t_x = Pong.DELTA
        self.t_y = Pong.DELTA
        
    def inWorldY(self):
        if self.ycor() < Pong.WORLD_YPOS-1.5*Pong.DELTA and self.ycor() > Pong.WORLD_YNEG+1.5*Pong.DELTA:
            return True
        else:
            return False
        
    def inWorldX(self):
        if self.xcor() < Pong.WORLD_XPOS+1.5*Pong.DELTA and self.xcor() > Pong.WORLD_XNEG-1.5*Pong.DELTA:
            return True
        else:
            return False

    def setupBall(self):
        if self.angle < 0:
            self.angle = random.randint(0, 89) # where to go
            self.setheading(self.angle)
        else:
            # bounce, complementary angle
            self.angle = -1 * self.angle
            self.t_y = -1 * Pong.DELTA
    
    def move(self):
        (new_x, new_y) = self.pos()
        time.sleep(0.1)
        if self.inWorldY():
            #print(f"{Pong.WORLD_YPOS-1.5*Pong.DELTA} vs {Pong.WORLD_YNEG+1.5*Pong.DELTA}")
            self.goto(self.t_x + new_x, self.t_y + new_y)
        else:
            #print(self.pos(), self.angle)
            #self.t_y = -1 * Pong.DELTA
            self.setupBall() #bounce
            self.goto(self.t_x + new_x, self.t_y + new_y)
        
    #def moveBall(self):
    #    keep_going = True
    #    self.setupBall() # turn angle
    #    time.sleep(0.1)
    #    while keep_going:
    #        (t_x, t_y) = self.pos()
    #        if t_y >= Pong.WORLD_YNEG+Pong.DELTA:
    #            self.forward(Pong.DELTA)
    #        else:
    #            self.setupBall() #bounce
    #            self.forward(Pong.DELTA)

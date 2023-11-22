# config constants for game
from turtle import Screen
screen = Screen()
class Pong():
    # world constants
    WORLD_WIDTH  = 800
    WOLRD_HEIGHT = 600
    DELTA        = 10
    WORLD_XPOS   = WORLD_WIDTH/2
    WORLD_XNEG   = -WORLD_XPOS
    WORLD_YPOS   = WOLRD_HEIGHT/2
    WORLD_YNEG   = -WORLD_YPOS
    WORLD_INNYP  = WORLD_YPOS-1.5*DELTA
    WORLD_INNYN  = WORLD_YNEG+1.5*DELTA
    WORLD_INNXP  = WORLD_XPOS+1.5*DELTA
    WORLD_INNXN  = WORLD_XNEG-1.5*DELTA
# turtle shape
Rectangle = ((-40,10),(40,10),(40,-10),(-40,-10))
# register shape
screen.register_shape('rectangle', Rectangle)
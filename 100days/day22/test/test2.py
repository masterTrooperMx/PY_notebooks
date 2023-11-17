from turtle import Screen, Turtle

screen = Screen()
# turtle shape
Rectangle = ((-40,10),(40,10),(40,-10),(-40,-10))
# register shape
screen.register_shape('rectangle', Rectangle)
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

# create player
class Player(Turtle):
    def __init__(self, x, y, shape: str = "rectangle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.goto(x=x, y=y)
        self.showturtle()
        self.color("white")
        self.penup()

    def turnUp(self):
        # don't leave world!
        delta_up = self.pos() + (0, DELTA)
        if delta_up[1] <= WORLD_YPOS-45: 
            self.goto(delta_up)
        else:
            print(self.pos())
        
    def turnDown(self):
        # don't leave world!
        delta_down = self.pos() + (0, -DELTA)
        if delta_down[1] >= WORLD_YNEG+45:
            self.goto(delta_down)
        else:
            print(self.pos())

player1 = Player(WORLD_XNEG+20, 10)
player2 = Player(WORLD_XPOS-30, -10)

# just listen to events
screen.listen()

screen.onkey(player1.turnUp, 'w')
screen.onkey(player1.turnDown, 'x')
screen.onkey(player2.turnUp, 'u')
screen.onkey(player2.turnDown, 'm')

# closing  eveything
screen.exitonclick()
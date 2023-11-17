from Classes.config import *
from Classes.Score import *
from Classes.Player import *
from Classes.Ball import *

# setup world and screen
scoreboard = Scoreboard()

r_paddle = Player(Pong.WORLD_XNEG+20, 10)
l_paddle = Player(Pong.WORLD_XPOS-30, -10)

ball = Ball()

# just listen to events
screen.listen()

screen.onkey(r_paddle.turnUp, 'w')
screen.onkey(r_paddle.turnDown, 'x')
screen.onkey(l_paddle.turnUp, 'u')
screen.onkey(l_paddle.turnDown, 'm')

game_over = False
ball.setupBall()
while not game_over:
    ball.move()
    print(f"b{ball.pos()}, lf{l_paddle.pos()}, d{ball.distance(l_paddle)}")
    if ball.xcor() >= 380 and abs(ball.distance(l_paddle)) < 60:
        # bounce
        ball.angle = 270 - ball.angle
        ball.setupBall()

# closing  eveything
screen.exitonclick()
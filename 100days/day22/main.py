from Classes.config import *
from Classes.Score import *
from Classes.Player import *
from Classes.Ball import *

# setup world and screen
scoreboard = Scoreboard()
screen.tracer(0)

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
    screen.update() # smooth move
    if ball.inWorldX() == True:
        ball.move()
        print(f"b{ball.pos()}, lf{l_paddle.pos()}, d{ball.distance(l_paddle)}, {ball.t_x}, {ball.t_y}")
        if ball.xcor() >= 380 and abs(ball.distance(l_paddle)) < 60:
            # bounce
            ball.setupBall()
    else:
        print("Ball out!!")
        game_over = True
        break

# closing  eveything
screen.exitonclick()
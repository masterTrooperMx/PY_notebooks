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
print(vars(Pong))

# just listen to events
screen.listen()

screen.onkey(r_paddle.turnUp, "w")
screen.onkey(r_paddle.turnDown, "x")
screen.onkey(l_paddle.turnUp, "Up")
screen.onkey(l_paddle.turnDown, "Down")

game_over = False
ball.setupBall()
while not game_over:
    screen.update() # smooth move
    if ball.inWorldX() == True:
        ball.move()
        print(f"b{ball.pos()}, lf{l_paddle.pos()}, d{ball.distance(l_paddle)}, {ball.t_x}, {ball.t_y}")
        if ball.xcor() >= 340 and abs(ball.distance(l_paddle)) < 65 or ball.xcor() <= -340 and abs(ball.distance(r_paddle)) < 65:
            # bounce
            print("Bounce!")
            ball.t_x *= -1
            ball.t_y *= -1
            ball.move()
    else:
        print("Ball out!!")
        game_over = True
        break

# closing  eveything
screen.exitonclick()
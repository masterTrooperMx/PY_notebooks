from Classes.Snake import *
from Classes.Food import *
from Classes.Score import *

score = Score()
snake = Snake()
# init snake
snake.setupScreen()
snake.createSnakeBody()
# init food
food = Food()

# just listen to events
snake.screen.listen()

snake.screen.onkey(snake.turnUp, 'Up')
snake.screen.onkey(snake.turnDown, 'Down')
snake.screen.onkey(snake.turnLeft, 'Left')
snake.screen.onkey(snake.turnRight, 'Right')

# move snake
while snake.keep_running:
    snake.screen.update()
    
    time.sleep(0.1)
    for t in reversed(snake.arr_turtles):
        ind = snake.arr_turtles.index(t)
        timmy = t
        if ind > 0:
            timmy_bef = snake.arr_turtles[ind-1]
            timmy.goto(timmy_bef.pos())
        else:
            # just the head
            timmy.forward(15)
            dist = timmy.distance(food)
            if dist <= NEAR:
                #print(f"{dist} eat")
                food.moveFood()
                # add score
                score.updateScore()
                # grow snake
                snake.growSnake()
            # game over options
            if timmy.xcor() > WORLD_XPOS or timmy.xcor() < WORLD_XNEG or timmy.ycor() > WORLD_YPOS or timmy.ycor() < WORLD_YNEG:
                #print(f"{WORLD_XPOS}-{WORLD_XNEG}-{WORLD_YPOS}-{WORLD_YNEG} {timmy.pos()}")
                score.writeGameOver()
                snake.keep_running = False
                break
            # if snake bites its own tail
            for part in snake.arr_turtles:
                if part.pos() == timmy.pos():
                    print(f"{part.pos()}, {timmy.pos()}")
                    pass
                #elif timmy.distance(part) < COLLIDE:
                else:
                    print(f"{timmy.distance(part)}")
                    #score.writeGameOver()
                    #snake.keep_running = False
                    #break
# closing  eveything
snake.screen.exitonclick()
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
            timmy.forward(15)
            dist = timmy.distance(food)
            if dist <= NEAR:
                #print(f"{dist} eat")
                food.moveFood()
                # add score
                score.updateScore()

# closing  eveything
snake.screen.exitonclick()
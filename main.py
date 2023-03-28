import random
from turtle import Turtle, Screen
from snake1 import Snake
import time

sc = Screen()
sc.setup(width=600, height=600)
sc.title("Snake Game")
sc.tracer(0)
sc.listen()

snake = Snake()

game_on = True

while game_on:
    sc.update()
    time.sleep(0.5)
    snake.move()
    sc.onkey(snake.up, "Up")
    sc.onkey(snake.down, "Down")
    sc.onkey(snake.left, "Left")
    sc.onkey(snake.right, "Right")


sc.exitonclick()


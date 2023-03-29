import random
from turtle import Turtle, Screen
from snake1 import Snake
from food import Food
import time
from score import Score

sc = Screen()
sc.setup(width=600, height=600)
sc.title("Snake Game")
sc.tracer(0)
sc.listen()

snake = Snake()
food = Food()
score = Score()

sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game_on = True

while game_on:
    sc.update()
    time.sleep(0.2)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 10:
        # snake.grow()
        food.refresh()
        score.increase_score()


sc.exitonclick()


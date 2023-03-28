from turtle import Turtle, Screen
import time


sc = Screen()
sc.screensize(600, 600)

snake = []
for i in range(3):
    snake.append("A" + str(i))


x = 0
y = 0
for i in range(len(snake)):
    snake[i] = Turtle()
    snake[i].penup()
    snake[i].shape("square")
    snake[i].color("black")
    snake[i].goto(x, y)
    x -= 20


def snake_move():
    for i in range(len(snake) -1, 0, -1):
        x1 = snake[i-1].xcor()
        y1 = snake[i-1].ycor()
        snake[i].goto(x1, y1)


def right_move():
    snake[0].right(90)


def left_move():
    snake[0].left(90)

def down_move():
    snake[0].right(90)

def up_move():
    snake[0].left(90)

start_game = True
while start_game:
    sc.listen()

    sc.onkey(key="Up", fun=up_move)
    sc.onkey(key="Right", fun=right_move)
    sc.onkey(key="Left", fun=left_move)
    sc.onkey(key="Down", fun=down_move)
    cont_move = True
    while cont_move:
        sc.update()
        time.sleep(0.3)
        snake_move()
        snake[0].forward(20)



sc.exitonclick()

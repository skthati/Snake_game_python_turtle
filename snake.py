from turtle import Turtle, Screen
import time

# t = Turtle()
sc = Screen()
# t.shape("square")
# t.color("blue")
sc.screensize(600, 600)

snake = []
for i in range(3):
    snake.append("A" + str(i))

sc.tracer(0)

x = 0
y = 0
for i in range(len(snake)):
    snake[i] = Turtle()
    snake[i].penup()
    snake[i].shape("square")
    snake[i].color("black")
    snake[i].goto(x, y)
    x -= 20

for i in range(10):
    sc.update()
    time.sleep(0.5)
    for i in range(len(snake)):
        snake[i].forward(20)
        sc.delay(100)

for i in range(1):
    sc.update()
    time.sleep(0.5)
    for i in range(len(snake)):
        snake[i].left(90)
        sc.delay(100)

for i in range(10):
    sc.update()
    time.sleep(0.5)
    for i in range(len(snake)):
        snake[i].forward(20)
        sc.delay(100)
    


sc.exitonclick()

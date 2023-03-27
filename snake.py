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

# sc.tracer(0)

x = 0
y = 0
for i in range(len(snake)):
    snake[i] = Turtle()
    snake[i].penup()
    snake[i].shape("square")
    snake[i].color("black")
    snake[i].goto(x, y)
    x -= 20

for i in range(2):
    sc.update()
    time.sleep(0.5)
    for i in range(len(snake)):
        snake[i].forward(20)
        sc.delay(100)

for i in range(1):
    # sc.update()
    # time.sleep(1)
    for i in range(len(snake)):
        if i == 0:
            snake[i].left(90)
            # snake[i].forward(20)
        if i == 1:
            snake[i-1].forward(20)
            snake[i].forward(20)
            snake[i].left(90)
            snake[i+1].forward(20)
            # snake[i].forward(20)
        if i == 2:
            snake[i-2].forward(20)
            snake[i-1].forward(20)
            snake[i].forward(20)
            snake[i].left(90)
            # snake[i].forward(20)
        # for j in range(int(i)):
        #     snake[i].forward(20)
        #     snake[i].left(90)
        # sc.delay(100)

for i in range(5):
    sc.update()
    time.sleep(0.5)
    for i in range(len(snake)):
        snake[i].forward(20)
        sc.delay(100)
    


sc.exitonclick()

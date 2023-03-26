from turtle import Turtle, Screen

# t = Turtle()
sc = Screen()
# t.shape("square")
# t.color("blue")
sc.screensize(600, 600)

snake = []
for i in range(3):
    snake.append("A" + str(i))

x = 0
y = 0
for i in snake:
    i = Turtle()
    i.shape("square")
    i.color("black")
    i.goto(x, y)
    x -= 20
    


    


sc.exitonclick()

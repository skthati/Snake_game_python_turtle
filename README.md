<a name="readme-top"></a>
# Snake Game

<div align="center">
<!-- Title: -->
<h1><a href="https://github.com/skthati/Turtle/">Snake Game</a> - Python Turtle </h1>
</div>

<!-- Table of contents -->
<hr>
<hr>
<ol>
    <li><a href="#basics">Basics</a> </li>
</ol>
<hr>
<hr>

<!-- Test1  -->
## Build Snake <a name="build_snake"></a>
Initial stage of snake.

1. Code
    ```Python
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
    for i in range(len(snake)):
        snake[i] = Turtle()
        snake[i].shape("square")
        snake[i].color("black")
        snake[i].goto(x, y)
        x -= 20

    for i in range(10):
        for i in range(len(snake)):
            snake[i].forward(20)

    sc.exitonclick()
    ```

2. Output
![Alt text](weird_snake_move_1.gif)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<hr>  

<!-- Test1  -->
## Better Snake <a name="better_snake"></a>
Make a better snake. Using screen tracer, delay and time sleep.

1. Code
    ```Python
    sc.tracer(0)

    for i in range(10):
        sc.update()
        time.sleep(0.5)
        for i in range(len(snake)):
            snake[i].forward(20)
            sc.delay(100)
    ```

2. Output
![Alt text](better_snake.gif)

[Full Code location](snake.py)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<hr>  




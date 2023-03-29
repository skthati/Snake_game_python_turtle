from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def reset_score(self):
        self.goto(0, 0)
        self.clear()
        self.write("Game Over", align="center", font=("Courier", 34, "normal"))
        # self.score = 0
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
        
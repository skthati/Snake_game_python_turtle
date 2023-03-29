from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake():
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_body = Turtle("square")
            new_body.color("black")
            new_body.penup()
            new_body.goto(position)
            self.body.append(new_body)

    
    def move(self):
        for b in range(len(self.body) - 1, 0, -1):
            x = self.body[b-1].xcor()
            y = self.body[b-1].ycor()
            self.body[b].goto(x, y)
        
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize()
        self.penup()
        self.setheading(30)

    def move_ball(self):
        self.speed("slowest")
        self.forward(10)
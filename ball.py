from turtle import Turtle
from utils import BALL_SPEED


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize()
        self.penup()

    def move_ball(self):
        self.speed("slowest")
        new_x = self.xcor() + BALL_SPEED
        new_y = self.ycor() + BALL_SPEED
        self.goto(new_x, new_y)

from turtle import Turtle
from utils import *


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setx(position)

    def go_up(self):
        new_y = self.ycor() + MOVEMENT_SPEED
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVEMENT_SPEED
        self.goto(self.xcor(), new_y)

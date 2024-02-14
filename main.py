from turtle import *

screen = Screen()
screen.title("PONG GAME")
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=600)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=4, stretch_len=0.5, outline=None)
paddle.penup()

print("bye world")
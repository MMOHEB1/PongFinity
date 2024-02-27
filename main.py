from utils import *
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("PONG GAME")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle(PADDLE_POSITION[0])
l_paddle = Paddle(PADDLE_POSITION[1])
ball = Ball()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    ball.move_ball()
    screen.update()
    # detecting collision with the wall:
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

#     detecting collision with the paddles:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        print("made contact")
        ball.bounce_x()


screen.exitonclick()

from utils import *
from turtle import Screen
from paddle import Paddle
from ball import Ball

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

screen.exitonclick()

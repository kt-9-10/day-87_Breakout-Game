from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle(0, -200)

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

ball = Ball()

is_game_continue = True
while is_game_continue:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO: 角に当たった時、挙動が変になる
    # Detect collision with paddle
    if paddle.pos()[0]-40 <= ball.pos()[0] <= paddle.pos()[0]+40 and paddle.pos()[1]-20 <= ball.pos()[1] <= paddle.pos()[1]+20:
        ball.bounce_y()

    # TODO: Create Block Class
    # TODO: Detect collision with Block
    # TODO: どのブロックとぶつかっているかをどう検知する？

screen.exitonclick()

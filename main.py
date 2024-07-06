from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

ball_size = 1
paddle_size_x = 6
paddle_size_y = 1
paddle_delta_x = paddle_size_x / 2 * 20 + ball_size / 2 * 20
paddle_delta_y = paddle_size_y / 2 * 20 + ball_size / 2 * 20

print((paddle_delta_x,paddle_delta_y))

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle(0, -200, paddle_size_x, paddle_size_y)

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

ball = Ball(ball_size)

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

    # Get paddle and ball position
    paddle_x, paddle_y = paddle.pos()
    ball_x, ball_y = ball.pos()

    # Set paddle collision
    paddle_col_left = paddle_x - paddle_delta_x
    paddle_col_right = paddle_x + paddle_delta_x
    paddle_col_bottom = paddle_y - paddle_delta_y
    paddle_col_top = paddle_y + paddle_delta_y

    # Detect collision with paddle
    if paddle_col_left < ball_x < paddle_col_right and paddle_col_bottom < ball_y < paddle_col_top:
        ball.bounce_by_paddle(paddle.towards(ball))

    # TODO: Create Block Class
    # TODO: Detect collision with Block
    # TODO: どのブロックとぶつかっているかをどう検知する？

screen.exitonclick()

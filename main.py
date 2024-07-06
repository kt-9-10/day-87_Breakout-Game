from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from block import Block
import time

ball_size = 1
paddle_size_x = 6
paddle_size_y = 1
paddle_delta_x = paddle_size_x / 2 * 20 + ball_size / 2 * 20
paddle_delta_y = paddle_size_y / 2 * 20 + ball_size / 2 * 20
block_size_x = 3.5
block_size_y = 1.5
block_delta_x = block_size_x / 2 * 20 + ball_size / 2 * 20
block_delta_y = block_size_y / 2 * 20 + ball_size / 2 * 20

block_pos_list = [
    (-360, 200), (-280, 200), (-200, 200), (-120, 200), (-40, 200), (40, 200), (120, 200), (200, 200), (280, 200), (360, 200),
    (-360, 160), (-280, 160), (-200, 160), (-120, 160), (-40, 160), (40, 160), (120, 160), (200, 160), (280, 160), (360, 160),
    (-360, 120), (-280, 120), (-200, 120), (-120, 120), (-40, 120), (40, 120), (120, 120), (200, 120), (280, 120), (360, 120),
    (-360, 80), (-280, 80), (-200, 80), (-120, 80), (-40, 80), (40, 80), (120, 80), (200, 80), (280, 80), (360, 80),
    (-360, 40), (-280, 40), (-200, 40), (-120, 40), (-40, 40), (40, 40), (120, 40), (200, 40), (280, 40), (360, 40)
]

print((paddle_delta_x,paddle_delta_y))

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.cv._rootwindow.resizable(False, False)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle((0, -200), paddle_size_x, paddle_size_y)

ball = Ball((0, -180), ball_size)

# Display Blocks
block_list = []
for block_pos in block_pos_list:
    block_list.append(Block(block_pos, block_size_x, block_size_y))

screen.listen()
screen.onkeypress(paddle.go_left, "a")
screen.onkeypress(paddle.go_right, "d")
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

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

    # Get ball position
    ball_x, ball_y = ball.pos()

    # Get paddle position
    paddle_x, paddle_y = paddle.pos()

    # Set paddle collision
    paddle_col_left = paddle_x - paddle_delta_x
    paddle_col_right = paddle_x + paddle_delta_x
    paddle_col_bottom = paddle_y - paddle_delta_y
    paddle_col_top = paddle_y + paddle_delta_y

    # Detect collision with paddle
    if paddle_col_left < ball_x < paddle_col_right and paddle_col_bottom < ball_y < paddle_col_top:
        ball.bounce_by_paddle(paddle.towards(ball))

    # TODO: Detect collision with Block
    for block in block_list:
        # Get block position
        block_x, block_y = block.pos()

        # Set block collision
        block_col_left = block_x - block_delta_x
        block_col_right = block_x + block_delta_x
        block_col_bottom = block_y - block_delta_y
        block_col_top = block_y + block_delta_y

        # Detect collision with block
        if block_col_left < ball_x < block_col_right and block_col_bottom < ball_y < block_col_top:
            if block_col_left < ball_x < block_col_right:
                ball.bounce_y()
            elif block_col_bottom < ball_y < block_col_top:
                ball.bounce_x()
            block.hideturtle()
            block_list.remove(block)


screen.exitonclick()

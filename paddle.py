from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos, paddle_size_x, paddle_size_y):
        super().__init__()

        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=paddle_size_y, stretch_len=paddle_size_x)
        self.goto(x_pos, y_pos)

    def go_left(self):
        if self.position()[0] <= -330:
            self.goto(-330, self.ycor())
        else:
            self.goto(self.xcor() - 10, self.ycor())

    def go_right(self):
        if self.position()[0] >= 330:
            self.goto(330, self.ycor())
        else:
            self.goto(self.xcor() + 10, self.ycor())

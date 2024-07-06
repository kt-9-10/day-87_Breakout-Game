from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos, size_x, size_y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=size_y, stretch_len=size_x)
        self.goto(pos[0], pos[1])

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

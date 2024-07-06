from turtle import Turtle


class Block(Turtle):
    def __init__(self, pos, size_x, size_y):
        super().__init__()
        self.penup()
        self.color("crimson")
        self.shape("square")
        self.shapesize(stretch_wid=size_y, stretch_len=size_x)
        self.goto(pos[0], pos[1])

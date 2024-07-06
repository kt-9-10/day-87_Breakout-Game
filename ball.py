from turtle import Turtle


class Ball(Turtle):

    def __init__(self, pos, size):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=size, stretch_len=size)
        self.x_move = 5
        self.y_move = 5
        self.setheading(self.towards(1, 1))
        self.move_speed = 0.03
        self.goto(pos[0], pos[1])

    def move(self):
        self.forward(8)

    def bounce_y(self):
        self.setheading(self.heading() * -1)

    def bounce_x(self):
        if 0 < self.heading() < 90:
            self.setheading(180 - self.heading())
        elif 90 < self.heading() < 180:
            self.setheading(self.heading() - (self.heading() - 90) * 2)
        elif 180 < self.heading() < 270:
            self.setheading(360 - (self.heading() - 180))
        elif 270 < self.heading() < 360:
            self.setheading(self.heading() - (self.heading() - 270) * 2)

    def bounce_by_paddle(self, direction):
        self.setheading(direction)

    def reset_position(self, x, y):
        self.goto(0, 0)
        self.setheading(self.towards(x, y))
        self.move_speed = 0.05

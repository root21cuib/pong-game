from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(3)
        self.goto(x=-280, y=0.0)
        self.shapesize(stretch_wid=0.5, stretch_len=3.0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)

    def up(self):
        self.setheading(90)
        self.forward(30)

    def down(self):
        self.setheading(270)
        self.forward(30)



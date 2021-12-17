from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()

    def dashup(self):
        for i in range(7):
            self.setheading(90)
            self.hideturtle()
            self.penup()
            self.forward(20)
            self.pendown()
            self.forward(20)
            self.penup()
            self.pensize(width=8)
            self.shape("square")
            self.color("white")

    def dashdown(self):
        for i in range(8):
            self.setheading(270)
            self.hideturtle()
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pensize(width=8)
            self.shape("square")
            self.color("white")


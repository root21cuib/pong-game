from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(2)
        self.goto(x=0.0, y=-210)
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(90)

    def slide(self):
        self.setheading(90)
        self.forward(40)
        self.left(90)
        self.forward(30)
        self.setheading(90)

    def move_right_up(self):
            self.forward(30)
            self.right(90)
            self.forward(20)
            self.setheading(90)

    def move_right_down(self):
        self.setheading(270)
        self.forward(30)
        self.left(90)
        self.forward(22)
        self.setheading(270)

    def move_left_down(self):
        self.setheading(270)
        self.forward(30)
        self.right(90)
        self.forward(22)
        self.setheading(270)







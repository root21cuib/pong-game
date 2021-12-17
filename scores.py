from turtle import Turtle


class Score1(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=-80, y=210)
        self.write(f"{self.score}", align="center", font=("Courier", 50, "normal"))
        self.hideturtle()

    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align="center", font=("Courier", 50, "normal"))



class Score2(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=80, y=210)
        self.write(f"{self.score}", align="center", font=("Courier", 50, "normal"))
        self.hideturtle()

    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align="center", font=("Courier", 50, "normal"))

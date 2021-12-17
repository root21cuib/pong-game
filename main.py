from turtle import Screen
import random
from cpu import Cpu
from scores import Score1, Score2
from my_player import Player
from line import Line
from ball import Ball
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
play = Player()
cpu = Cpu()
sc1 = Score1()
sc2 = Score2()
ball = Ball()
lin = Line()
screen.onkeypress(key="Up", fun=play.up)
screen.onkeypress(key="Down", fun=play.down)
lin.dashup()
lin.goto(x=0.0, y=30.0)
lin.dashdown()
screen.listen()
not_score = True
refresh = True
right_down = True
left_down = False
while not_score:
    screen.update()
    time.sleep(0.15)
    cpu.move()
    if ball.distance(play) < 40 or refresh is not True:
        refresh = False
        # ball.goto(0, 0)
        if right_down is True:
          ball.move_right_down()
        if ball.ycor() < -280 or right_down is False:
            right_down = False
            ball.move_right_up()
            if ball.xcor() > 300:
                sc1.increase()
                refresh = True
                right_down = True
                ball.goto(x=0.0, y=-210)
                play.goto(x=-280, y=0)
                cpu.goto(x=280, y=random.randint(-250, 250))
            elif ball.distance(cpu) < 32 or left_down is True:
                left_down = True
                ball.move_left_down()
                if ball.ycor() < -280:
                    refresh = True
                    left_down = False
                    right_down = True
                    # play.goto(x=-280, y=0)

    elif refresh is True:
        ball.slide()

    if ball.xcor() < -300:
        sc2.increase()
        play.goto(x=-280, y=0)
        ball.goto(x=0.0, y=-200.0)
        cpu.goto(x=280, y=random.randint(-250, 250))
    if cpu.ycor() > 260:
        cpu.setheading(270)
    if cpu.ycor() < -240:
        cpu.setheading(90)

screen.exitonclick()

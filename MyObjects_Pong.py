from turtle import Turtle
from time import sleep


class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.shapesize(5,1)
        self.goto(x,y)

    def move_up(self):
        yn = self.ycor()
        if yn > 250:
            self.ycor(yn)
        yn += 30
        self.sety(yn)

    def move_down(self):
        yn = self.ycor()
        if yn < -250:
            self.ycor(yn)
        yn -= 30
        self.sety(yn)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed(0)
        self.dx, self.dy = 5, 5

    def dxdy(self):
        x = self.xcor() + self.dx
        y = self.ycor() + self.dy
        self.goto(x, y)

    def bounce(self,side):
        if side == "y":
            self.dy *= -1
        elif side == "x":
            self.dx *= -1

    def open_set(self):
        self.goto(0, 0)
        sleep(0.5)
        self.bounce("x")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.scoreA, self.scoreB = 0, 0

    def print_score(self,playerAname,playerBname):
        self.clear()
        self.write("{} : {}     {} : {}".format(playerAname,self.scoreA,playerBname,self.scoreB),align='center',font=('Courier', 20, 'normal'))

    def point(self,player):
        if player == "A":
            self.scoreA += 1
        if player == "B":
            self.scoreB += 1

    def scoreA(self):
        return self.scoreA

    def scoreB(self):
        return self.scoreB




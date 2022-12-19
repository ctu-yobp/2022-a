from turtle import Screen
from MyObjects_Pong import Paddle, Score, Ball

sc = Screen()
sc.bgcolor("black")
scwidth, scheight = 1000, 600
sc.setup(scwidth,scheight)


padA = Paddle(-450,0) #leva
padB = Paddle(450,0) #prava
ball = Ball()
ball.open_set()

sc.listen()
sc.onkeypress(padA.move_up,'w')
sc.onkeypress(padA.move_down,'s')
sc.onkeypress(padB.move_up,'Up')
sc.onkeypress(padB.move_down,'Down')

score = Score()
playerAname = "playerA"
playerBname = "playerB"
score.print_score(playerAname=playerAname,playerBname=playerBname)

# main loop
while True:
    sc.update()

    # pohyb mice
    ball.dxdy()

    # naraz mice spodek/vrsek
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("y")

    # naraz mice leva/prava
    if ball.xcor() < -480:
        ball.open_set()
        score.point("B")
        score.print_score(playerAname=playerAname,playerBname=playerBname)

    if ball.xcor() > 480:
        ball.open_set()
        score.point("A")
        score.print_score(playerAname=playerAname,playerBname=playerBname)

    # naraz mice paddle A
    if (ball.xcor() > -450 and ball.xcor() < -440) and (ball.ycor() < padA.ycor()+50 and ball.ycor() > padA.ycor()-50):
        ball.bounce("x")
    
    # naraz mice paddle B
    if (ball.xcor() > 440 and ball.xcor() < 450) and (ball.ycor() < padB.ycor()+50 and ball.ycor() > padB.ycor()-50):
        ball.bounce("x")


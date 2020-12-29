from turtle import Turtle, Screen
from referee import Referee
from pad import Pad
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor('black')
screen.title('Pong')
screen.setup(width=800, height=500)
screen.tracer(0)

ref = Referee()
ref.draw_line()

pad1 = Pad(-350, 0)
pad2 = Pad(350, 0)

screen.listen()
screen.onkeypress(pad2.up, 'Up')
screen.onkeypress(pad2.down, 'Down')
screen.onkeypress(pad1.up, 'a')
screen.onkeypress(pad1.down, 'z')

ball = Ball()
score = Score()

screen.update()
screen.tracer(1)

while True:
    ball.move()

    if(ball.xcor() >= -350 and ball.xcor() <= -340 and ball.ycor() <= pad1.ycor()+40 and ball.ycor() >= pad1.ycor()-40):
        screen.tracer(0)
        ball.setheading(180-ball.heading())
        screen.update()
    if(ball.xcor() <= 350 and ball.xcor() >= 340 and ball.ycor() <= pad2.ycor()+40 and ball.ycor() >= pad2.ycor()-40):
        screen.tracer(0)
        ball.setheading(180-ball.heading())
        screen.update()
    if(ball.xcor() < -350):
        screen.tracer(0)
        score.update_p1()
        ball.goto(0, 0)
        ball.setheading(-125)
        screen.update()
    if(ball.xcor() > 350):
        screen.tracer(0)
        score.update_p2()
        ball.goto(0, 0)
        ball.setheading(125)
        screen.update()
    screen.tracer(1)

screen.exitonclick()

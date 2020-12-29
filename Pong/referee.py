from turtle import Turtle


class Referee(Turtle):
    xcor, ycor = 0, 255

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.setheading(270)
        self.pensize(5)
        self.penup()
        self.goto(self.xcor, self.ycor)

    def draw_line(self):
        while(self.ycor >= -250):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
            self.ycor -= 40

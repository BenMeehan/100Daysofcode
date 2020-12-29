from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color('white')
        self.shape('circle')
        self.speed('slowest')
        self.setheading(125)
        self.penup()

    def move(self):
        self.check_bounds()
        self.forward(50)

    def check_bounds(self):
        y = self.ycor()
        self._tracer(0)
        if(y >= 230 or y <= -230):
            self.setheading(-self.heading())
        self._update()
        self._tracer(1)

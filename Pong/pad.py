from turtle import Turtle


class Pad(Turtle):
    def __init__(self, xc, yc):
        super().__init__()
        self.xc = xc
        self.yc = yc
        self.color('white')
        self.penup()
        self.goto(xc, yc)
        self.shape('square')
        self.speed('fastest')
        self.shapesize(stretch_len=0.5, stretch_wid=2)

    def up(self):
        self.yc += 20
        self.goto(self.xc, self.yc)

    def down(self):
        self.yc -= 20
        self.goto(self.xc, self.yc)

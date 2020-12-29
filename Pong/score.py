from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 200)
        self.p1 = 0
        self.p2 = 0
        self.hideturtle()
        self.write(f'{self.p1}\t{self.p2}', align='center',
                   font=('Arial', 15, 'normal'))

    def update_p1(self):
        self.clear()
        self.p2 += 1
        self.write(f'{self.p1}\t{self.p2}', align='center',
                   font=('Arial', 15, 'normal'))

    def update_p2(self):
        self.clear()
        self.p1 += 1
        self.write(f'{self.p1}\t{self.p2}', align='center',
                   font=('Arial', 15, 'normal'))

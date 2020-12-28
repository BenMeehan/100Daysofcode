from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.total = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.color('white')
        self.write_score()

    def write_score(self):
        self.write(arg='Score = '+str(self.total),
                   align='center', font=("Arial", 15, "normal"))

    def increment_score(self):
        self.clear()
        self.total += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER\nPress Y to play again.',
                   align='center', font=("Arial", 25, "normal"))

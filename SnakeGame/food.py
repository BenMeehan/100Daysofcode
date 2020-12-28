from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.shape('circle')
        self.penup()
        self.speed('fastest')
        self.new_location()

    def new_location(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)

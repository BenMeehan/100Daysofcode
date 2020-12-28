from turtle import Turtle


class Snake:
    START_POS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    segments = []

    def __init__(self):
        for i in self.START_POS:
            self.add_segment(i)

    def add_segment(self, position):
        snake_seg = Turtle()
        snake_seg.color('white')
        snake_seg.shape('square')
        snake_seg.penup()
        snake_seg.setpos(position)
        self.segments.append(snake_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            xcor = self.segments[seg-1].xcor()
            ycor = self.segments[seg-1].ycor()
            self.segments[seg].goto((xcor, ycor))

        self.segments[0].forward(self.MOVE_DISTANCE)

    def up(self):
        if(self.segments[0].heading() != 270):
            self.segments[0].setheading(90)

    def down(self):
        if(self.segments[0].heading() != 90):
            self.segments[0].setheading(270)

    def left(self):
        if(self.segments[0].heading() != 0):
            self.segments[0].setheading(180)

    def right(self):
        if(self.segments[0].heading() != 180):
            self.segments[0].setheading(0)

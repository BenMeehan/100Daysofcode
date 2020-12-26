from turtle import Turtle, Screen, textinput
import random


def generate_turtles(colors):
    '''Generate different turtles. Takes a list of colors as argument and returns a list of Turtle objects.'''
    turtles = []
    for i in colors:
        timmy1 = Turtle()
        timmy1.shape('turtle')
        timmy1.color(i)
        turtles.append(timmy1)
    return turtles


def set_turtles_initial(turtles):
    '''Move the turtles to their initial position. Takes a list of Turtle objects as argument.'''
    x = -320
    y = -150
    for i in turtles:
        i.penup()
        i.goto(x, y)
        # i.pendown()
        y += 50


def move_turtles(turtles):
    '''Move the turtles forward by a random number. Takes a list of Turtle objects as input and returns the winner.'''
    while True:
        for i in turtles:
            i.forward(random.randint(1, 10))
            if(i.xcor() >= 320):
                return i.color()[0]


screen = Screen()
screen.setup(width=800, height=600)

color = textinput(
    "Make Your Bet", "Who will win the race? Enter a rainbow color ")

colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
turtles = generate_turtles(colors)

set_turtles_initial(turtles)
winner = move_turtles(turtles)

if(color == winner):
    print("You win! "+winner+" is the winner.")
else:
    print("You Lose! "+winner+" is the winner.")

screen.exitonclick()

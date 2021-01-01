from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
image = './india.gif'

screen.bgpic(image)
screen.setup(626, 734)

screen.listen()
screen.title('Guess the state')

timmy = Turtle()
timmy.penup()
timmy.hideturtle()

df = pd.read_csv('./states.csv')
states = df.states.to_list()
answered = []

game_not_over = True

while game_not_over:
    inp = screen.textinput(title='Enter the state',
                           prompt='Enter a state name. Type Q to Exit')

    if(inp == 'q' or inp == 'Q'):
        game_not_over = False

    else:
        if(inp.title() in states):
            answered.append(inp)
            st = df[df['states'] == inp.title()]
            x = int(st['x'])
            y = int(st['y'])
            timmy.goto(x, y)
            timmy.write(inp.title())

            if(len(answered) == len(states)):
                game_not_over = False

        else:
            pass


screen.exitonclick()

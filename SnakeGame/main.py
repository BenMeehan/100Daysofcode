from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.bgcolor('black')
screen.setup(600, 600)
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'Right')

game_not_over = True

while game_not_over:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if(snake.segments[0].distance(food) < 15):
        food.new_location()
        snake.extend()
        score.increment_score()

    if snake.segments[0].xcor() <= -300 or snake.segments[0].xcor() >= 300 or snake.segments[0].ycor() <= -300 or snake.segments[0].ycor() >= 300:
        game_not_over = False
        score.game_over()

    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 5:
            game_not_over = False
            score.game_over()


screen.exitonclick()

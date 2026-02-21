# This Snake Game Improved
#There is a high score that is saved to an external file so it can be perpetual
# The input delay is terrible btw

from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.reset() #changed game over to reset
        snake.reset() #reset snake to the center
        food.refresh()

    # Detect collision with tail

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset() #changed game over to reset
            snake.reset() #reset snake to the center
            food.refresh()

screen.exitonclick()

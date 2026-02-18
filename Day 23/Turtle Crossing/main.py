import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# Screen setup
screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

# Game objects
player = Player()
score = Scoreboard()
car_manager = CarManager()

# listening to keyboard inputs
screen.listen()
screen.onkey(player.go_up, "Up")


# main loop

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.spawn_car()
    car_manager.move()

    # reaching the top (score)
    if player.finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.increase_score()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()


screen.exitonclick()
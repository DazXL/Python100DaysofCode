FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.current_level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.current_level}", align="center", font=FONT)

    def increase_score(self):
        self.current_level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
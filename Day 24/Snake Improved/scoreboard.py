# This is how the Score is written on the screen
# Also game over message
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read()) #high_score added using external file
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 240)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # Game Over function changed to reset function
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(f"{self.high_score}"))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
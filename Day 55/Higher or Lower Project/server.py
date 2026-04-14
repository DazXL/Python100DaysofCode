from flask import Flask
import random


app = Flask(__name__)


@app.route("/")
def hello_world():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")

@app.route("/<int:number>")
def guess_number(number):
    random_number = random.randint(0, 9)
    if number == random_number:
        return ("<h1>It is the same number! That's odd!</h1>"
                "<img src='https://media0.giphy.com/media/v1"
                ".Y2lkPTc5MGI3NjExeTlna3Q1amQ2MzRwMGR1YW8wZm"
                "tvaDBxdnBsbXoya21pdWEwaHh4bCZlcD12MV9pbnRlcm"
                "5hbF9naWZfYnlfaWQmY3Q9Zw/M6439cC6oOTpcc2bU5/"
                "giphy.gif'>")
    elif number > random_number:
        return (f"<h1>It is higher than the number {random_number} you win!</h1>"
                "<img src='https://media2.giphy.com/media/v1"
                ".Y2lkPTc5MGI3NjExNjNjZmNhMzEyY3VlcDRzMjFqbGN"
                "6eTVlank4dnk4ZzdvZmdqZ3A2MSZlcD12MV9pbnRlcm5h"
                "bF9naWZfYnlfaWQmY3Q9Zw/EzGQJwS4x8cHxjJhEH/giphy.gif'>")
    else:
        return (f"<h1>It is lower than the number {random_number} you lose!</h1>"
                f"<img src='https://media0.giphy.com/media/v1"
                f".Y2lkPTc5MGI3NjExeW9reXExeXNyanc0eTEzNWpvdzB"
                f"kczUydWFlZWdobTFuZWI4c2QxaCZlcD12MV9pbnRlcm5h"
                f"bF9naWZfYnlfaWQmY3Q9Zw/piTERt2CEdrLt2WLv0/giphy.gif'>")

if __name__ == "__main__":
    app.run(debug=True)

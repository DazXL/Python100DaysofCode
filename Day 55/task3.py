#Challenge: Use Python Decorators to Style HTML Tags
from flask import Flask

def make_bold(func):
    def bold():
        get_bold = func()
        return f"<b>{get_bold}</b>"
    return bold

def make_emphasis(func):
    def emphasis():
        get_emphasis = func()
        return f"<em>{get_emphasis}</em>"
    return emphasis

def make_underlined(func):
    def underlined():
        get_underlined = func()
        return f"<u>{get_underlined}</u>"
    return underlined

app = Flask(__name__)
@app.route("/")
def hello_world():
    return ("<h1 style='text-align:center'>Hello, World!</h1>"
            "<p>this is a paragraph</p>"
            "<img src='https://media4.giphy.com/media/v1"
            ".Y2lkPTc5MGI3NjExa3F6ZjF2bjh6aW90NzR6Mzh4Y3A0c2gxM2RxNz"
            "FvbG9wdHp2eWkycyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw"
            "/XjXXDwkTMtl1S/giphy.gif'>")

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_goodbye():
    return "Bye!"

@app.route("/username/<name>")
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)
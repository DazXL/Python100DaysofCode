#Rendering HTML Elements with Flask
from flask import Flask

app = Flask(__name__)

#this function will render a Header, a paragraph and an animated gif in the page
@app.route("/")
def hello_world():
    return ("<h1 style='text-align:center'>Hello, World!</h1>"
            "<p>this is a paragraph</p>"
            "<img src='https://media4.giphy.com/media/v1"
            ".Y2lkPTc5MGI3NjExa3F6ZjF2bjh6aW90NzR6Mzh4Y3A0c2gxM2RxNz"
            "FvbG9wdHp2eWkycyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw"
            "/XjXXDwkTMtl1S/giphy.gif'>")

if __name__ == "__main__":
    app.run(debug=True)


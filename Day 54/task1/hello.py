#The name of the file cannot have the same name as the framework or library you're working with
from flask import Flask #pip install Flask

app = Flask(__name__) #attributes the variable app with Flask()

@app.route("/") #route of the app "/" means main page
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__": #runs the app from the script instead of terminal
    app.run()
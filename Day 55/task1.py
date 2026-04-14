#Working Flask URL Paths and the Flask Debugger
from flask import Flask #pip install Flask

app = Flask(__name__) #attributes the variable app with Flask()

@app.route("/") #route of the app "/" means main page
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_goodbye():
    return "<p>Bye!</p>"

@app.route("/username/<name>") #URL path using the <name> value creates a variable
def greet(name):
    return f"Hello, {name}!" #if I add /username/DazXL as an example, the variable will be attributed DazXL

if __name__ == "__main__": #runs the app from the script instead of terminal
    app.run(debug=True) #turns on debug which makes it easier to work with Flask during development

#if changing anything in the file and saving it the flask server is refreshed and ready to be tested.
#path variables have to be created the right way, strings cannot have a forward slash
#path variables are strings by default
#but if you want the slash to a string just add /<path:name>
#if you want to add an integer add /<int:number>
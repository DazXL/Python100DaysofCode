#This is the America's States Game
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U. S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv("50_states.csv")
correct_answers = states.state.to_list()
guessed_states = []

while len(guessed_states) < len(correct_answers):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's Another state's name?").title()

    if answer_state == "Exit":
        '''This parte of the code was updated in Day 26 to ad List Comprehension'''
        missing_states = [state for state in correct_answers if state not in guessed_states]
        # for state in correct_answers:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in correct_answers:
        if state == answer_state:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = states[states.state == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state)

turtle.mainloop()


"""
this is a code to get coordinates on the screen when you click
I will later make a brazil states game

# def get_mouse_click_coor(x, y):
#     print(x, y)
# 
# turtle.onscreenclick(get_mouse_click_coor)


"""
from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

try:
    words_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    words_dict = original_data.to_dict(orient="records")
else:
    words_dict = words_data.to_dict(orient="records")

current_card = {}

#---------------------------LOGIC-----------------------------#
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(title_label, text = "French", fill="black")
    canvas.itemconfig(word_label, text = current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title_label, text = "English", fill = "white")
    canvas.itemconfig(word_label, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_image, image = card_back_img)

def is_known():
    words_dict.remove(current_card)
    words_learn = pd.DataFrame(words_dict)
    words_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ----------------------- UI --------------------------------#

#window
window = Tk()
window.title("Flashy")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

#card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file = "Images/card_front.png")
card_back_img = PhotoImage(file = "Images/card_back.png")

card_image = canvas.create_image(400, 263, image=card_front_img) #background

title_label = canvas.create_text(400, 150, text = "Title", font=("Arial", 40, "italic")) #title label

word_label = canvas.create_text(400, 263, text = "Word", font=("Arial", 60, "bold")) #word label

canvas.grid(row=0, column=0, columnspan=2)

#buttons

v_image = PhotoImage(file = "Images/right.png")
v_button = Button(image=v_image, highlightthickness=0, command=is_known)
v_button.grid(row=2, column=1)

x_image = PhotoImage(file = "Images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=next_card)
x_button.grid(row=2, column=0)

next_card()
window.mainloop()
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

from numpy import number

with open("config.json") as file:
    data = json.load(file)

EMAIL = data["email"]

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if website_entry.get() == "" or pass_entry.get() == "" or email_entry.get() == "":
        messagebox.showerror("Error", "Please enter all fields")

    else:
        is_ok = messagebox.askokcancel(title="Password Manager", message=f"These are the details you entered:\n"
                                                                 f"Email: {email_entry.get()}\n Password: {pass_entry.get()}")
        if is_ok:
            with open("data.txt", "a") as pass_file:
                pass_file.write(f"{website_entry.get()} | {email_entry.get()} | {pass_entry.get()}\n")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)
                website_entry.focus()
            messagebox.showinfo("Password Manager", "You have successfully saved")

# ---------------------------- UI SETUP ------------------------------- #



# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#image
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#labels
website_label = Label(window, text="Website:")
website_label.grid(row=1, column=0)

email_username_label = Label(window, text="Email/Username:")
email_username_label.grid(row=2, column=0)

password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=52)
email_entry.insert(0, EMAIL)
email_entry.grid(row=2, column=1, columnspan=2)

pass_entry = Entry(width=34)
pass_entry.grid(row=3, column=1)

#button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


# loop
window.mainloop()
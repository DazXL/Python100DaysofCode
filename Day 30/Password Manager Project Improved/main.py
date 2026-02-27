"""Adding JSON support and error handling and search button to the project"""
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

with open("config.json") as file:
    config = json.load(file)

EMAIL = config["email"]

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
    website = website_entry.get().upper()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website)== 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror("Error", "Please enter all fields")

    else:
        try:
            with open("data.json", "r") as pass_file:
                #opens the data
                pass_data = json.load(pass_file)

        except FileNotFoundError:
            with open("data.json", "w") as pass_file:
                json.dump(new_data, pass_file, indent=4)

        else:
            #updating with new data
            pass_data.update(new_data)

            with open("data.json", "w") as pass_file:
                #writing the new data
                json.dump(pass_data, pass_file, indent=4)

        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            website_entry.focus()

        messagebox.showinfo("Password Manager", "You have successfully saved")

# --------------------------- FIND PASSWORD --------------------------- #

def find_password():
    find_website = website_entry.get().upper()

    try:
        with open("data.json", "r") as pass_file:
            find_data = json.load(pass_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "There is no data file yet.")
    else:
        if find_website in find_data:
            find_email = find_data[find_website]["email"]
            find_pass = find_data[find_website]["password"]
            messagebox.showinfo("Password Manager", f"Your info for the site: {find_website}:\n "
                                                        f"email: {find_email}\n password: {find_pass}")
            pyperclip.copy(find_pass)
        else:
                messagebox.showinfo("Error", f"{find_website} not found")

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
website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=52)
email_entry.insert(0, EMAIL)
email_entry.grid(row=2, column=1, columnspan=2)

pass_entry = Entry(width=34)
pass_entry.grid(row=3, column=1)

#button
generate_button = Button(text="Generate Password", command=generate_password, width=14)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=find_password, width=14)
search_button.grid(row=1, column=2)

# loop
window.mainloop()
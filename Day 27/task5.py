#Task 5 is more TKinter around pack, place and grid

from tkinter import *

#Window

window = Tk()
window.title("Hello World")
window.minsize(500, 300)

#Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
#my_label.pack() #limited positioning
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button
def button_clicked():
    print("button clicked")
    if input_text.get() != "":
        new_text = input_text.get()
        my_label.config(text=new_text)

button = Button(text="Click Me!", command=button_clicked)
#button.place(x=40, y=40) #way too specific
button.grid(column=1, row=1)

new_button = Button(text="New Button!", command=button_clicked)
new_button.grid(column=2, row=0)

#Entry https://www.tcl-lang.org/man/tcl8.6/TkCmd/entry.htm

input_text = Entry()
print(input_text.get())
input_text.grid(column=2, row=2) # considers the screen as a grid, and you can set in places
# you get an error if you try to mix grid and pack

window.mainloop() #keeps the window open

window.mainloop()
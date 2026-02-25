#Task 3 is more TKinter

from tkinter import *

window = Tk()
window.title("Hello World")
window.minsize(500, 300)

#Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button
def button_clicked():
    print("Button clicked!")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me!", command=button_clicked)
button.pack()

#Entry https://www.tcl-lang.org/man/tcl8.6/TkCmd/entry.htm

input = Entry()
input.pack()

window.mainloop() #keeps the window open
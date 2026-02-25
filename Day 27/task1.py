#Task 1 is about the TKinter

import tkinter # https://docs.python.org/3/library/tkinter.html

window = tkinter.Tk() #creates a window
window.title("My first GUI program")
window.minsize(500, 300)

#Label

my_label = tkinter.Label(window, text="Hello World", font=("Arial", 24, "bold"))
my_label.pack() #packs the label to the screen, check the tkinter doc on pack()










window.mainloop() #keeps the window open
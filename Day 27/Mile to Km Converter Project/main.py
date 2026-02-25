#Mile do Km Converter Project

from tkinter import *

def miles_to_km():
    miles = float(input_text.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


#Entry
input_text = Entry(width=7)
input_text.grid(row=0, column=1)

#Labels
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label= Label(text="is equal to")
equal_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

kilometers_label = Label(text="kilometers")
kilometers_label.grid(row=1, column=2)


#Button
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(row=2, column=1)


window.mainloop()
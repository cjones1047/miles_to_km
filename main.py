from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

miles_entry = Entry()
miles_entry.grid(column=2, row=1)

miles_label = Label()
miles_label.grid(column=3, row=1)

equals_label = Label()
equals_label.grid(column=1, row=2)

km_output = Label()
km_output.grid(column=2, row=2)

km_label = Label()
km_label.grid(column=3, row=2)

calculate_button = Button()
calculate_button.grid(column=2, row=3)

window.mainloop()

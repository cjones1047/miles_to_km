from tkinter import *

FONT = ("Arial", 24, "normal")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=10, pady=20)


def convert_m_to_km():
    int_miles = float(miles_entry.get())
    km = round(int_miles * 1.6, 1)
    if km == 0:
        km = int(km)
    km_output.config(text=km)


miles_entry = Entry(width=5)
miles_entry.insert(END, string='0')
miles_entry.focus()
miles_entry.grid(column=2, row=1)

miles_label = Label(text="miles", font=FONT)
miles_label.grid(column=3, row=1)

equals_label = Label(text="is equal to", font=FONT)
equals_label.grid(column=1, row=2)

km_output = Label(text=0, font=FONT)
km_output.grid(column=2, row=2)

km_label = Label(text="km", font=FONT)
km_label.grid(column=3, row=2)

calculate_button = Button(text="Calculate", command=convert_m_to_km)
calculate_button.grid(column=2, row=3)

window.mainloop()

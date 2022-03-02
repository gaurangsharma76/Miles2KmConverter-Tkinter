from tkinter import *


def miles2km():
    miles = miles_input.get()
    km = 1.609 * float(miles)
    km_value_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km converter")

window.minsize(width=200, height=100)
window.config(padx=20, pady=20)
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_to = Label(text="equals")
equal_to.grid(column=0, row=1)

km_value_label = Label(text=0)
km_value_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

Calculate_Button = Button(text="Calculate",command=miles2km)
Calculate_Button.grid(column=1, row=2)

window.mainloop()

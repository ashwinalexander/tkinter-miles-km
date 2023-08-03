from tkinter import *
import turtle

window = Tk()

window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


# Entry / An Input effectively
input_miles = Entry()
input_miles.config(width = 10)
input_miles.grid(column=1,row=0)

# Label - miles
label_miles = Label(text="Miles", font=("Arial", 12))
label_miles.grid(row=0,column=2)

# Label - is equal to
label_equal = Label(text="is equal to", font=("Arial", 12))
label_equal.grid(row=1,column=0)

# Label - calculated num
label_calc = Label(text="0", font=("Arial", 12))
label_calc.grid(row=1,column=1)

# Label - km
label_km = Label(text="km", font=("Arial", 12))
label_km.grid(row=1,column=2)


#Button - calculate
def button_clicked():
    kms_val = float(input_miles.get()) * 1.60934
    label_calc.config(text=round(kms_val, 2))


button_calc = Button(text="Calculate", command= button_clicked)
button_calc.grid(row=2, column=1)

window.mainloop()





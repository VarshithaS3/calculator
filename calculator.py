from tkinter import*

# Create the main window
root = Tk()
root.title("Modern Calculator")
root.geometry("400x360")  # Set the window size to 400x360
root.configure(bg="#33ffcc")  # Set the background color


# Create the entry field for the calculation
calculation_entry= Entry(root, width=35, borderwidth=5)
calculation_entry.grid(row=0, column=0, columnspan=4)

# Define the append_to_entry function
def append_to_entry(value):
    current_entry = calculation_entry.get()
    calculation_entry.delete(0, END)
    calculation_entry.insert(0, str(current_entry) + str(value))

# Define the calculate function
def calculate():
    try:
        result = eval(calculation_entry.get())
        calculation_entry.delete(0, END)
        calculation_entry.insert(0, result)
    except:
        calculation_entry.delete(0, END)
        calculation_entry.insert(0, "Error")

# Define the clear function
def clear():
    calculation_entry.delete(0, END)

# Create the number buttons
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: append_to_entry("7"))
button_7.grid(row=1, column=0)
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: append_to_entry("8"))
button_8.grid(row=1, column=1)
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: append_to_entry("9"))
button_9.grid(row=1, column=2)
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: append_to_entry("/"))
button_divide.grid(row=1, column=3)

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: append_to_entry("4"))
button_4.grid(row=2, column=0)
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: append_to_entry("5"))
button_5.grid(row=2, column=1)
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: append_to_entry("6"))
button_6.grid(row=2, column=2)
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: append_to_entry("*"))
button_multiply.grid(row=2, column=3)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: append_to_entry("1"))
button_1.grid(row=3, column=0)
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: append_to_entry("2"))
button_2.grid(row=3, column=1)
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: append_to_entry("3"))
button_3.grid(row=3, column=2)
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: append_to_entry("-"))
button_subtract.grid(row=3, column=3)

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: append_to_entry("0"))
button_0.grid(row=4, column=0)
button_decimal = Button(root, text=".", padx=40, pady=20, command=lambda: append_to_entry("."))
button_decimal.grid(row=4, column=1)
button_equals = Button(root, text="=", padx=40, pady=20, command=calculate)
button_equals.grid(row=4, column=2)
button_add = Button(root, text="+", padx=40, pady=20, command=lambda: append_to_entry("+"))
button_add.grid(row=4, column=3)

# Create the clear button
button_clear = Button(root, text="Clear", padx=79, pady=20, command=clear)
button_clear.grid(row=5, column=0, columnspan=4)

# Start the main loop
root.mainloop()
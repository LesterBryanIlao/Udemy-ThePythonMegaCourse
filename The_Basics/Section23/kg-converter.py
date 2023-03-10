from tkinter import *
import time
# Create an empty Tkinter window
window = Tk()


def clear_all_text_box():
    t1.delete("1.0", END)
    t2.delete("1.0", END)
    t3.delete("1.0", END)
    

def print_invalid_values_message():
    t1.insert(END, "Invalid value!")
    t2.insert(END, "Invalid value!")
    t3.insert(END, "Invalid value!")
    
def from_kg():
    # Empty the Text boxes if they had text from the previous use and fill them again
    # Deletes the content of the Text box from start to END
    clear_all_text_box()
    
    try:
        # Get user value from input box and multiply by 1000 to get kilograms
        gram = float(e2_value.get())*1000

        # Get user value from input box and multiply by 2.20462 to get pounds
        pound = float(e2_value.get())*2.20462

        # Get user value from input box and multiply by 35.274 to get ounces
        ounce = float(e2_value.get())*35.274
        
        # Fill in the text box with the value of gram variable
        t1.insert(END, f"{gram} gram/s")
        t2.insert(END, f"{pound} pound/s")
        t3.insert(END, f"{ounce} ounce/s")
        
    except:
        print_invalid_values_message()


# Create a Label widget with "Kg" as label
e1 = Label(window, text="Kg")
e1.grid(row=0, column=0)  # The Label is placed in position 0, 0 in the window

e2_value = StringVar()  # Create a special StringVar object
# Create an Entry box for users to enter the value
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

# Create a button widget
# The from_kg() function is called when the button is pushed
b1 = Button(window, text="Convert", command=from_kg)
b1.grid(row=0, column=2)

# Create three empty text boxes, t1, t2, and t3
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

# This makes sure to keep the main window open
window.mainloop()

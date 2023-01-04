from tkinter import *
import time
window = Tk()

def km_to_miles():
    
    t1.delete("1.0", END)
    t1.selection_clear()
    
    try:    
        miles=float(e1_val.get())*1.6
        t1.insert(END, miles)
    except:
        t1.insert(END, "Invalid value!")
        
        
    

b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0, column=1)


t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)
window.mainloop()

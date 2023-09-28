#code is close to creating a basic Tkinter window with labels, entry widgets, and a submit button.
from tkinter import *

root = Tk()
root.geometry('250x250')

# Create labels
username_label = Label(root, text="Username")
password_label = Label(root, text="Password")

# Create entry widgets
t1 = Entry(root)
t2 = Entry(root)

# Create a submit button
b1 = Button(root, text="Submit")

# Use the grid layout to place widgets
username_label.grid(row=0, column=0)
t1.grid(row=0, column=1)

password_label.grid(row=1, column=0)
t2.grid(row=1, column=1)

b1.grid(row=2, column=1)  # Adjust the row and column as needed

root.mainloop()


#other way
#username = Label(root,text="Username",).grid(row=0,column=0)
#t1 = Entry(root).grid(row=0,column=1)




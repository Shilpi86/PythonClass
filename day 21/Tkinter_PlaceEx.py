from tkinter import *
root = Tk()
root.geometry('300x300')

# Create labels
username_label = Label(root, text="Username")
password_label = Label(root, text="Password")

# Create entry widgets
t1 = Entry(root) #boxes are given as Entry
t2 = Entry(root)

# Create a submit button
b1 = Button(root, text="Submit")
b2 = Button(root, text="Register")
# Use the place layout to place widgets
username_label.place(x=30, y=50)
t1.place(x=100, y=50)

password_label.place(x=30, y=100)
t2.place(x=100, y=100)

b1.place(x=30, y=150)  # Adjust the row and column as needed
b2.place(x=190, y=150)
root.mainloop()
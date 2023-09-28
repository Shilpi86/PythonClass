from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('250x250')

v1=IntVar()

def m1():
    selected_option = v1.get()
    if selected_option == 1:
        messagebox.showinfo("Selection", "You selected Mango")
    elif selected_option == 2:
        messagebox.showinfo("Selection", "You selected Apple")
    elif selected_option == 3:
        messagebox.showinfo("Selection", "You selected Orange")

r1 = Radiobutton(root,text="Mango", variable=v1, value=1, command = m1)
r2 = Radiobutton(root,text="Apple", variable=v1, value=2, command = m1)
r3 = Radiobutton(root,text="Orange", variable=v1, value=3, command = m1)

r1.pack()
r2.pack()
r3.pack()

root.mainloop()


# OR


# rom tkinter import *
# from tkinter import messagebox

# root = Tk()
# root.geometry('250x250')

# v1=IntVar()

# def m1():
    # select = "Selected option is "+str(v1.get()) #v1.get()
    # lb.config(text=select)

# r1 = Radiobutton(root,text="Mango", variable=v1, value=1, command = m1) #value='mango'
# r2 = Radiobutton(root,text="Apple", variable=v1, value=2, command = m1)
# r3 = Radiobutton(root,text="Orange", variable=v1, value=3, command = m1)

# r1.pack()
# r2.pack()
# r3.pack()


# lb = Label(root)
# lb.pack()

# root.mainloop()
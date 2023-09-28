from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('250x250')

v1=IntVar()

def m1():
    select = "Selected option is "+str(v1.get()) #v1.get()
    lb.config(text=select)

r1 = Radiobutton(root,text="Mango", variable=v1, value=1, command = m1) #value='mango'
r2 = Radiobutton(root,text="Apple", variable=v1, value=2, command = m1)
r3 = Radiobutton(root,text="Orange", variable=v1, value=3, command = m1)

r1.pack()
r2.pack()
r3.pack()


lb = Label(root)
lb.pack()

root.mainloop()
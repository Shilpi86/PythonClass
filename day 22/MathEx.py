# to create a simple Tkinter GUI application that calculates the sum of two numbers entered in
# text entry fields and displays the result when a button is pressed.

from tkinter import *
# from tkinter import messagebox
from functools import partial

root = Tk()
root.geometry('250x250')

def m1(lbResult, N1, N2):
    num1 = int(N1.get())  # Convert the input to integers
    num2 = int(N2.get())
    result = num1 + num2
    lbResult.config(text="Result = %d" % result)

N1 = StringVar()
N2 = StringVar()

lb1 = Label(root, text="Num1")
lb2 = Label(root, text="Num2")
lbResult = Label(root)

lb1.grid(row=1, column=0)
lb2.grid(row=2, column=0)
lbResult.grid(row=8, column=2)

e1 = Entry(root, textvariable=N1)
e2 = Entry(root, textvariable=N2)

e1.grid(row=1, column=2)
e2.grid(row=2, column=2)

m1 = partial(m1, lbResult, N1, N2)
b1 = Button(root, text="Add", command=m1)
b1.grid(row=3, column=0)

root.mainloop()

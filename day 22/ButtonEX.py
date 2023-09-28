from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('250x250')

# define a function

def m1():
    #messagebox.showinfo("Message","You have clicked the message")
 # or
    text = "you have clicked the button"
    messagebox.showinfo("Message",text)

#b1 = Button(root, text='Click', command=m1).pack()
#or
b1 = Button(root, text='Click',command=root.destroy)
b1.pack()
root.mainloop()
#kinter-based calculator application that allows users to perform basic arithmetic operations.
# It includes buttons for digits (0-9), arithmetic operators (+, -, *, /), a clear button (C), and an equals button (=).
from tkinter import *

root = Tk()
root.geometry('480x280')
root.resizable(0,0) # cannot do any maximize or resize
#root.maxsize(700,700) # can maximize the screen upto one level
root.title("Calculator")

def btn_click(value): #if 7 is entered that goes to variable "value"
    global data
    data = data+str(value) #that value is concatenated with data
    itext.set(data) # itext is the variable which is created for inputText(text box)

def btn_clear():
    global data
    data=""
    itext.set(data)

def btn_equals():
    global data
    result=str(eval(data))
    itext.set(result)

data = "" # that data is empty,thus 7 will be entered in the textbox
itext = StringVar()

# Creating separate frame for text box.
inputFrame = Frame(root,bg='gray',width=400,height=100)
inputFrame.pack(side=TOP)

#Text box for the data insertion
inputText =Entry(inputFrame,textvariable=itext,width=45,font=('times new roman',20,'bold'),justify=RIGHT)
inputText.grid(row=0,column=0)
inputFrame.pack()

# Creating separate frame for butttons.
btnsFrame = Frame(root,bg='lavender',width=50,height=150)
btnsFrame.pack()

#Calculator buttons creation
# lambda=  btn_click function using lambda. it takes as single functionality.
nine = Button(btnsFrame,text="9", width=9, height=3, command=lambda:btn_click(9)).grid(row=1,column=0)
eight = Button(btnsFrame,text="8", width=9, height=3, command=lambda:btn_click(8)).grid(row=1,column=1)
seven = Button(btnsFrame,text="7", width=9, height=3, command=lambda:btn_click(7)).grid(row=1,column=2)
plus = Button(btnsFrame,text="+", width=9, height=3, command=lambda:btn_click("+")).grid(row=1,column=3)

six = Button(btnsFrame,text="6", width=9, height=3, command=lambda:btn_click(6)).grid(row=2,column=0)
five = Button(btnsFrame,text="5", width=9, height=3, command=lambda:btn_click(5)).grid(row=2,column=1)
four = Button(btnsFrame,text="4", width=9, height=3, command=lambda:btn_click(4)).grid(row=2,column=2)
minus = Button(btnsFrame,text="-", width=9, height=3, command=lambda:btn_click("-")).grid(row=2,column=3)

three = Button(btnsFrame,text="3", width=9, height=3, command=lambda:btn_click(3)).grid(row=3,column=0)
two = Button(btnsFrame,text="2", width=9, height=3, command=lambda:btn_click(2)).grid(row=3,column=1)
one = Button(btnsFrame,text="1", width=9, height=3, command=lambda:btn_click(1)).grid(row=3,column=2)
Mul = Button(btnsFrame,text="*", width=9, height=3, command=lambda:btn_click("*")).grid(row=3,column=3)

clear = Button(btnsFrame,text="C", width=9, height=3, command=lambda:btn_clear()).grid(row=4,column=0)
zero = Button(btnsFrame,text="0", width=9, height=3, command=lambda:btn_click(0)).grid(row=4,column=1)
equals = Button(btnsFrame,text="=", width=9, height=3, command=lambda:btn_equals()).grid(row=4,column=2)
div = Button(btnsFrame,text="/", width=9, height=3, command=lambda:btn_click("/")).grid(row=4,column=3)

root.mainloop()
#geometry
#pack: left right top bottom
#Grid: rows and columns
#Place: x and y coords

#Tkinter depends on widgets(button,checkboxes,radio button,entry, framebox,textbox,message,listbox,label,scrollbar etc

#---------------------------------------------------------------------------------------------------------------------#

from tkinter import *
root = Tk()
root.geometry('250x250')

lb = Button(root, text='Left',height=2,width=5,fg="black")
lb.pack(side=LEFT)
rb = Button(root, text='Right',height=2,width=5,fg="blue")
rb.pack(side=RIGHT)
tb = Button(root, text='Top',height=2,width=5,fg="green")
tb.pack(side=TOP)
bb = Button(root, text='Bottom',height=2,width=5,fg="violet")
bb.pack(side=BOTTOM)
root.mainloop()
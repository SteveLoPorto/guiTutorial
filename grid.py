from tkinter import *

#creat a root, window
root = Tk()

#creates a label object
myLabel1 = Label(root, text="Hellow World!")
myLabel2 = Label(root, text="My Name is Steven LoPorto!")
myLabel3 = Label(root, text="                ")

#how to inject the label into the root
myLabel1.grid(row=0, column = 0)
myLabel2.grid(row=1, column = 5)
myLabel3.grid(row=1, column = 1)


#create an event loop to constanly run to look for input
root.mainloop()
from tkinter import *

#creat a root, window
root = Tk()

#creates a label object
myLabel = Label(root, text="Hellow World!")

#how to inject the label into the root
myLabel.pack()

#create an event loop to constanly run to look for input
root.mainloop()
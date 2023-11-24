from tkinter import *

#creat a root, window
root = Tk()

def myClick():
  myLabel = Label(root, text="look i clicked button")
  myLabel.pack()

myButton = Button(root, text="Click Me!", pady=20, command=myClick, fg="blue", bg="red")
myButton.pack()




#create an event loop to constanly run to look for input
root.mainloop()
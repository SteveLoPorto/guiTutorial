from tkinter import *

#creat a root, window
root = Tk()

e = Entry(root, width=50, borderwidth="20")
e.pack()


def myClick():
  
  myLabel = Label(root, text= "Hello " + e.get())
  myLabel.pack()

myButton = Button(root, text="Enter Your Name!", pady=20, command=myClick, fg="blue", bg="red")
myButton.pack()




#create an event loop to constanly run to look for input
root.mainloop()
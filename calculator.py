from tkinter import *

#creat a root, window
root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=90, borderwidth=5, text="enter a number")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#declare globals for the add function
prevNumber = None
operation = None 

def button_click(number):
  current = e.get()
  e.delete(0, END)
  e.insert(0, current + str(number))
  return
  
def button_clear():
  global operation
  global prevNumber
  if(operation != None and e.get() == ""):
    operation = None
  if(operation == None and prevNumber!=None and e.get() == ""):
    prevNumber = None
  e.delete(0, END)
  return

def button_add():
  global operation
  global prevNumber
  prevNumber = e.get()
  if(prevNumber == ""):
    return
  operation = "add"
  e.delete(0, END)
  return

def button_subtract():
  global operation
  global prevNumber
  prevNumber = e.get()
  if(prevNumber == ""):
    return
  operation = "subtract"
  e.delete(0, END)
  return

def button_multiply():
  global operation
  global prevNumber
  prevNumber = e.get()
  if(prevNumber == ""):
    return
  operation = "multiply"
  e.delete(0, END)
  return

def button_divide():
  global operation
  global prevNumber
  prevNumber = e.get()
  if(prevNumber == ""):
    return
  operation = "divide"
  e.delete(0, END)
  return

def button_equals():
  global operation
  global prevNumber
  if(operation == "add"):
    currentNum = int(e.get())
    prevNumber = int(prevNumber)
    e.delete(0, END)
    e.insert(0, (prevNumber + currentNum))
    operation = None
    prevNumber = None
  if(operation == "subtract"):
    currentNum = int(e.get())
    prevNumber = int(prevNumber)
    e.delete(0, END)
    e.insert(0, (prevNumber - currentNum))
    operation = None
    prevNumber = None
  if(operation == "multiply"):
    currentNum = int(e.get())
    prevNumber = int(prevNumber)
    e.delete(0, END)
    e.insert(0, (prevNumber * currentNum))
    operation = None
    prevNumber = None
  if(operation == "divide"):
    currentNum = int(e.get())
    prevNumber = int(prevNumber)
    e.delete(0, END)
    e.insert(0, (prevNumber / currentNum))
    operation = None
    prevNumber = None
  if(operation == None or prevNumber == None):
    currentNum = int(e.get())
    operation = None
    prevNumber = None

  return 
    


#define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)
button_equals = Button(root, text="=", padx=40, pady=50, command=button_equals)
button_clear = Button(root, text="Clear", padx=32, pady=50, command=button_clear)

#put buttons on screen

button_add.grid(row=1, column=0, padx=1, pady=1, sticky="nsew")
button_subtract.grid(row=1, column=1, padx=1, pady=1, sticky="nsew")
button_divide.grid(row=1, column=2, padx=1, pady=1, sticky="nsew")
button_multiply.grid(row=1, column=3, padx=1, pady=1, sticky="nsew")

button_7.grid(row=2, column=0, padx=1, pady=1, sticky="nsew")
button_8.grid(row=2, column=1, padx=1, pady=1, sticky="nsew")
button_9.grid(row=2, column=2, padx=1, pady=1, sticky="nsew")

button_4.grid(row=3, column=0, padx=1, pady=1, sticky="nsew")
button_5.grid(row=3, column=1, padx=1, pady=1, sticky="nsew")
button_6.grid(row=3, column=2, padx=1, pady=1, sticky="nsew")

button_1.grid(row=4, column=0, padx=1, pady=1, sticky="nsew")
button_2.grid(row=4, column=1, padx=1, pady=1, sticky="nsew")
button_3.grid(row=4, column=2, padx=1, pady=1, sticky="nsew")

button_0.grid(row=5, column=1, padx=1, pady=1, sticky="nsew")

button_clear.grid(row=2, column=3, rowspan=2, padx=1, pady=1, sticky="nsew")
button_equals.grid(row=4, column=3, rowspan=2, padx=1, pady=1, sticky="nsew")



#create an event loop to constanly run to look for input
root.mainloop()
from tkinter import *

root = Tk()

e = Entry(root, width = 50, bg = 'blue', fg = 'white')
e.pack()
#e.get()
e.insert(0, 'Enter your Name here: ')

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

myButton = Button(root, text = "Click Me!", command = myClick, fg = 'blue') #state = DISABLED, padx = 50, pady = 50)
myButton.pack()

root.mainloop()
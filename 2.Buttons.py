from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = "Look! I clicked a Button!")
    myLabel.pack()

myButton = Button(root, text = "Click Me!", command = myClick, fg = 'blue') #state = DISABLED, padx = 50, pady = 50)
myButton.pack()

root.mainloop()
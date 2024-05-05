from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", padx=300, pady=200, command=myClick, fg="#FF0000", bg="#FF0000")
myButton.pack()
root.mainloop()
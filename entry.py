from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
e.pack()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", padx=30, command=myClick, fg="#FF0000", bg="#FF0000")
myButton.pack()
root.mainloop()
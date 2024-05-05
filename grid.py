from tkinter import *

root = Tk()

# grid 的位置是相对的 relative
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is John Elder")
myLabel3 = Label(root, text="My label 3")
myLabel4 = Label(root, text="My label 4")
myLabel5 = Label(root, text="My label 5")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)
myLabel4.grid(row=1, column=2)
myLabel5.grid(row=1, column=3)
root.mainloop()